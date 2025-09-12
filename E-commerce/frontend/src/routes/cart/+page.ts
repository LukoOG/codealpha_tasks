export const load = async ({locals, fetch, parent}) => {
	let cart = {}
	const { user } = await parent()
	console.log(user)

	
	return { cart }
}