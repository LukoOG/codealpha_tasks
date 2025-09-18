const load = async ({ cookies, parent }) => {
	const { user } = await parent();
	
	return {
		user
	}
}