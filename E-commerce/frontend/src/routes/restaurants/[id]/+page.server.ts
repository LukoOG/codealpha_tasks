import type { Actions } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';
import { PUBLIC_BACKEND_URL } from "$env/static/public";

export const load = async ({ params, parent }) => {
	const { restaurants } = await parent();
	
	const restaurant = restaurants.find((r: any) => String(r.id) === params.id);

    if (!restaurant) {
        throw new Error("Restaurant not found");
    }

    return {
        restaurant
    };
}

export const actions: Actions = {
	add: async({ request, cookies }) => {
		if(!cookies.get("accessToken")){
			redirect(303,'/auth?form_state=login')
		}
		const data = await request.formData()
		const product = data.get("product")
		
        const res = await fetch(
            `${PUBLIC_BACKEND_URL}/api/cart-items/`,
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json",
					"Authorization": `Bearer ${cookies.get("accessToken")}`
                },
                body:JSON.stringify({ product, quantity:1 })
            }
        )
		
		if(res.ok){
			const data = await res.json()
			console.log(data)
		}
		//console.log(res)
	}
}