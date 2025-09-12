import type { Handle } from "@sveltejs/kit";
import jwt from "jsonwebtoken"; // or any JWT lib
import { JWT_SECRET } from "$env/static/private"

export const handle: Handle = async ({ event, resolve }) => {
  const access = event.cookies.get("accessToken");
  
  if (access) {
    try {
      const user = jwt.decode(access);
      event.locals.user = user; // available in +page.server.ts
    } catch(err){
	    console.error(err)
		event.locals.user = null;
    }
  }else{
	  event.locals.user = null;
  }

  return resolve(event);
};
