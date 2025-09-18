import { PUBLIC_BACKEND_URL } from "$env/static/public"

export const load = async ({ fetch }) => {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/api/users/${params.username}`)
	if(res.ok){
		const data = await res.json()
		return {
			user: data
		}
	}
}