import { PUBLIC_BACKEND_URL } from "$env/static/public"

export const load = async ({ cookies, fetch }) => {
	const access = cookies.get("accessToken");
	const res = await fetch(`${PUBLIC_BACKEND_URL}/api/posts/`, {
		headers:{
			"Access-Control-Allow-Origin":"127.0.0.1:8000",
			"Authorization": `Bearer ${access}`,
			
		}
	})
	
	if (res.ok){
		const data = await res.json()
		return {
			posts: data.results,
			next: data.next,
			previous: data.previous,
		}
	}
}