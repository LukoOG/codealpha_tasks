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

interface Item{
	id: number,
    product: {
      id: number,
      name: string,
      description: string,
      price: string,
      image: string,
      available: true
    },
    quantity: number,
    total_price: number
}

export type cartData = {
	restaurant: number,
    restaurant_name: string,
    status: string,
    items: Item[],
    created_at: string,
    updated_at: string
}