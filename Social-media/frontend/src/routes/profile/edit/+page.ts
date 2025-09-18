import { PUBLIC_BACKEND_URL } from "$env/static/public"
import { error, redirect } from '@sveltejs/kit';


export const load = async ({cookies, fetch, parent }) => {
	const { user } = await parent()
	if(!user){
		throw redirect(303, "/auth")
	}	
	let res = await fetch(`${PUBLIC_BACKEND_URL}/api/users/me`,{
		headers:{
			"Authorization":`Bearer ${cookies.get("accessToken")}`
		}
	})
	if(res.ok){
		const data = await res.json()
		return {
			profiles: data
		}
	}
}