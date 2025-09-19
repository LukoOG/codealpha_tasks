import { PUBLIC_BACKEND_URL } from "$env/static/public"
import { error, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const load = async ({cookies, fetch, parent }) => {
	const { user } = await parent()
	if(!user){
		throw redirect(303, "/auth")
	}

	try{

		let res = await fetch(`${PUBLIC_BACKEND_URL}/api/users/me/`,{
			headers:{
				"Authorization": `Bearer ${cookies.get("accessToken")}`
			}
		})
		if(res.ok || res.status==200){
			const data = await res.json()
			return { userData:data }
		} else{
			return error(res.status, { error: "failed to fetch cart" });
		}
	}catch(error){
		console.error(error)
		console.log(error)
	}
	return redirect(303, '/')
}

export const actions: Actions = {
  update: async ({ request, cookies, locals }) => {
    console.log(locals.user.username);

    // 1. Read form data
    const formData = await request.formData();

    // Convert formData to plain object
    const data: Record<string, any> = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    // 2. Get access token from cookies
    const accessToken = cookies.get("accessToken");
    if (!accessToken) {
      return {
        error: "Not authenticated",
      };
    }

    try {
      // 3. Send PATCH request to Django
      const res = await fetch(`${PUBLIC_BACKEND_URL}/api/users/${locals.user.username}/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        const error = await res.json();
        return { error };
      }

      const updatedUser = await res.json();
	  
	  cookies.delete("accessToken", { path: "/" });
      return {
        success: true,
        user: updatedUser,
		forceRefresh: true,
      };
    } catch (err) {
      console.error("Update failed:", err);
      return {
        error: "Something went wrong",
      };
    }
  },
};