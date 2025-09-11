import type { restaurantData } from "$lib/types.ts"

class RestaurantsCache{
	#cache = $state<{ [id:number]:restaurantData }>({})
	
	constructor(){}
	
	add(id:number, data: restaurantData){
		this.cache = { ...this.cache, [id]:data	}
	}
	
	remove(id:number){
		const { [id]: _, ...rest } = this.cache
		this.cache = rest
	}
	
	getRestaurantCache(id:number){
		return this.cache?.[id] ?? null
	}
	
	clearCache(){
		this.cache = {}
	}
}

export const restaurantsCache = new RestaurantsCache()