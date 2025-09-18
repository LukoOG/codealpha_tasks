import { PUBLIC_BACKEND_URL } from "$env/static/public"

export const load = async ({ fetch }) => {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/api/users`)
	if(res.ok){
		const data = await res.json()
		return {
			profiles: data.results
		}
	}
}