import type { restaurantData, cartData } from "$lib/types.ts"

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

//Primarily to be able to share state in order to retrieve itemcount in navbar
class CartCache{
	#cache = $state<cartData[]>([])
	constructor(){}
	
	create(data:cartData){
		this.cache = data
	}
	
	
	getItemCount(){
		if(this.cache.length <= 0){
			return 0
		}
		const total = this.cache.reduce((t, curr)=>{
			const sumCurrItems = curr.items.reduce((t, innerCurr)=>t+innerCurr.quantity,0)
			return sumCurrItems
		}, 0)
		return total
	}
	
	clearCache(){
		this.cache = []
	}	
}

//export let cartCache = new CartCache()

export let cartItemsCount = $state({
	value:0,
	change(v){
		this.value = v
	}
	})