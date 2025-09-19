import { PUBLIC_BACKEND_URL } from "$env/static/public";
import type { Actions } from "./$types";


//Optimization: only fetch userData and move posts and followers fetch to client side then cache like in E-commerce

export const load = async ({ cookies, parent, params, fetch, locals }) => {
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

export const actions: Actions = {
    toggle_follow: async ({ params, cookies }) => {
        const access = cookies.get("accessToken");
        if (!access) {
            return { error: "Not authenticated" };
        }

        const res = await fetch(`${PUBLIC_BACKEND_URL}/api/users/${params.username}/toggle_follow/`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${access}`,
                "Content-Type": "application/json"
            }
        });

        if (!res.ok) {
            return { error: "Failed to follow user" };
        }
		const data = await res.json()
        return { success: true, following: data.following, no_follows:data.follows };
    }
};
