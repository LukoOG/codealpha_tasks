interface Category{
	id: number,
	name: string,
	items: {
		available: boolean,
		description: string,
		id: number,
		image: string,
		name: string,
		price: number,
	}[]
}

export type restaurantData = {
	categories: Category[]
}