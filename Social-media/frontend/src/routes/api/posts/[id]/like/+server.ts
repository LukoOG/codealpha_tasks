import type { RequestHandler } from './$types';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import { json } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ params, cookies }) => {
    const access = cookies.get("accessToken");
    if (!access) {
        return new Response(JSON.stringify({ error: "Not authenticated" }), { status: 401 });
    }

    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/posts/${params.id}/toggle_like/`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${access}`,
            "Content-Type": "application/json"
        }
    });
	if(!res.ok){
		return { error:"failed to like post" }
	}
	const { liked, likes} = await res.json()
	const data = { liked: liked, likes:likes }
    return new Response(JSON.stringify(data), {
		headers: {
			"Content-Type":"application/json"
		}
	});
};

export const DELETE: RequestHandler = async ({ params, cookies }) => {
    const access = cookies.get("accessToken");
    if (!access) {
        return new Response(JSON.stringify({ error: "Not authenticated" }), { status: 401 });
    }

    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/posts/${params.id}/like/`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${access}`,
            "Content-Type": "application/json"
        }
    });

    return json(await res.text(), { status: res.status });
};
