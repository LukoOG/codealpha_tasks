import type { Handle } from "@sveltejs/kit";
import jwt from "jsonwebtoken"; 
import { JWT_SECRET } from "$env/static/private"

import refreshAccessToken from "$lib/helpers/refreshAccessToken"

export const handle: Handle = async ({ event, resolve }) => {
	let access = event.cookies.get("accessToken");
	
	if(access){
		try{
			const user = jwt.decode(access);
			event.locals.user = user;			
		}catch(error){
			console.warn(error)
			console.warn("Access expired, attempting refresh...");
			console.log("Access expired, attempting refresh...");
			access = await refreshAccessToken(event);
			
			if (access) {
				const user = jwt.decode(access);
				event.locals.user = user;
			} else {
				event.locals.user = null;
			}
		}
	} else {
		access = await refreshAccessToken(event);
		event.locals.user = access ? jwt.verify(access, JWT_SECRET) : null;
	}
	return resolve(event);
};
