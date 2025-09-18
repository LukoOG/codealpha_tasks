import { PUBLIC_BACKEND_URL } from "$env/static/public"

export const load = async ({ cookies, parent, params, locals }) => {
	//TODO: combine both endpoints into 1
	const postRes = await fetch(`${PUBLIC_BACKEND_URL}/api/posts/?username=${params.username}`)
	const userRes = await fetch(`${PUBLIC_BACKEND_URL}/api/users/${params.username}`)
	const followersRes = await fetch(`${PUBLIC_BACKEND_URL}/api/users/${params.username}/following/`)
	
	if (postRes.ok && userRes.ok){
		const postData = await postRes.json()
		const userData = await userRes.json()
		const followers = await followersRes.json()
		return {
			posts: postData.results,
			userData,
			followers,
			next: postData.next,
			previous: postData.previous,
		}
	}
}