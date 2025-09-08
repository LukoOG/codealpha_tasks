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