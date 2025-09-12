import { PUBLIC_BACKEND_URL } from "$env/static/public";
import { error, redirect } from '@sveltejs/kit';

export const load = async ({cookies, fetch, parent}) => {
	let cart = {}
	const { user } = await parent()
	if(!user){
		throw redirect(303, "/restaurants")
	}	
	
	try{
		let res = await fetch(`${PUBLIC_BACKEND_URL}/api/cart/`,
			{
				headers: {
					"Authorization": `Bearer ${cookies.get("accessToken")}`
				}
			}
		)
		if(res.ok || res.status==200){
			const data = await res.json()
			cart = data
		} else{
			return error(res.status, { error: "failed to fetch cart" });
		}
	}catch(error){
		console.error(error)
	}
	return { cart }
}

export const actions: Actions = {
	
}