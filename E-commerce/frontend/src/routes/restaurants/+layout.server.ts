import { PUBLIC_BACKEND_URL } from "$env/static/public";

export const load = async ({ fetch, locals }) => {
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/restaurants/`)
	const restaurants = await res.json()
	return {
		restaurants: restaurants
	}
}