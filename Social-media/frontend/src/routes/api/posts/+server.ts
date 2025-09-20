import type { RequestHandler } from './$types';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import { json, redirect } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ params, cookies, request }) => {
    const access = cookies.get("accessToken");
    if (!access) {
        return new Response(JSON.stringify({ error: "Not authenticated" }), { status: 401 });
		redirect(303, '/auth')
    }
	
	const formData = await request.formData()
	//console.log(formData)

    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/posts/`, {
        method: "POST",
        headers: {
            "Authorization": access ? `Bearer ${access}` : ""
        },
		body: formData
    });
	if(!res.ok){
		console.log(await res.json())
		return new Response(JSON.stringify({ error:"failed to create post" }))
	}
	
	const data = await res.json()
    return new Response(JSON.stringify(data), {
		headers: {
			"Content-Type":"application/json"
		}
	});
};