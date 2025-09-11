<script lang='ts'>
	import { onMount } from 'svelte';
	import sleep from "$lib/helpers/sleep.ts";

	import { goto } from "$app/navigation";
	import { page } from "$app/state";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	import gsap from "gsap";
	
	import MenuCard from "$lib/components/restaurants/menuCard.svelte";
	import { restaurantsCache } from "$lib/global/cache.svelte.ts";
	
	import type { restaurantData } from "$lib/types.ts"
	
	let { data } = $props()
	let { restaurant } = data
	let menuContainer
	let menus = $state({})
	
	const extractCategories = async  (restaurantData: restaurantData) => {
		const data = await restaurantData
		for(const category of data.categories){
			categories.push(category.name)
		}
	}
	
	const filterMenu = (menus:any) => {
		
		if(selectedCategory === "All"){
			return menus
		}else if(selectedCategory !== "All"){
			return {categories: menus.categories.filter((category)=>category.name.toLowerCase() === selectedCategory.toLowerCase())}
		}else{
			return false
		}
	}
	
	let selectedCategory = $state("All")
	const categories = $state<string[]>(["All"])
	let filteredMenu = $derived.by(()=>filterMenu(menus))	
	
	$inspect("menu",filteredMenu)
	
	onMount(async ()=>{
		const cached = restaurantsCache.getRestaurantCache(restaurant.id)
		//check if cached
		if(cached){
			menus = cached
			console.log("using cache")
			extractCategories(menus)
		}else if(!cached){
			filteredMenu = false
			let res =  await fetch(`${PUBLIC_BACKEND_URL}/api/restaurants/${page.params.id}/`)
			await sleep(1500)
			if(res.ok){
				menus = await res.json()
				restaurantsCache.add(restaurant.id, menus)
				extractCategories(menus)
			}
			console.log("using fetch")
		}
	})
	
</script>
{#snippet CategoryFilters(category: string)}
	<button class={`px-4 py-2 rounded-full cursor-pointer whitespace-nowrap transition-colors ${
                selectedCategory === category
                  ? 'bg-restaurant-primary text-restaurant-primary-foreground'
                  : 'bg-secondary text-secondary-foreground hover:bg-restaurant-primary/20'
              }`}
              onclick={() => selectedCategory = category}
            >
              {category}
	</button>
{/snippet}

<section class="min-h-screen bg-background">
	<!-- Header -->
	<div class="relative">
		<div class="aspect-[16/6] overflow-hidden">
			<img
			src={"http://localhost:8000/media/banner.jpg"}
			alt={restaurant.name}
			class="w-full h-full object-cover"
			/>
		</div>
        
        <button onclick={()=>goto("/restaurants")} class="absolute top-4 left-4 bg-background/80 text-foreground p-2 rounded-full hover:bg-background transition-colors">
          ← Back
        </button>
        
		<div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-background/90 to-transparent p-6">
			<h1 class="text-4xl font-bold text-card-foreground mb-2">
				{restaurant.name}
			</h1>
			
			<p class="text-lg text-muted-foreground mb-4">
				{restaurant.description}
			</p>
          
			<div class="flex items-center gap-6 text-sm">
				<div class="flex items-center gap-1">
					<span class="text-restaurant-accent">⭐</span>
					<span class="font-medium text-card-foreground">{restaurant.avg_rating}</span>
				</div>
				
				<div class="text-muted-foreground">
					{restaurant.delivery_time}
				</div>
				
				<div class="text-muted-foreground">
					${restaurant.delivery_fee} delivery
				</div>
			</div>
		</div>
	</div>
	
	<!-- Menu -->
	<div class="max-w-7xl mx-auto px-6 py-8">
		<!-- Category Filter -->
		<div class="flex gap-2 mb-8 overflow-x-auto pb-2">
		{#if filteredMenu}
			{#each categories as category}
				{@render CategoryFilters(category)}
			{/each}
		{/if}
		</div>

		<!-- Menu Items -->
		<div bind:this={menuContainer} class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#if !filteredMenu}
				<!-- Skeleton loader -->
				<div class="animate-pulse mt-6">
				  <div class="h-6 bg-gray-300 rounded w-full mb-4"></div>
				  <div class="gap-4">
					<div class="bg-gray-200 rounded-lg h-48"></div>
				  </div>
				</div>
			{:else}
				{#each filteredMenu.categories as category, i (category.id)}
					{#each category.items as item (item.id)}
						<div class="bg-card rounded-lg overflow-hidden border border-border">
						
							<div class="aspect-video overflow-hidden">
								<img src={item.image} alt={item.name} class="w-full h-full object-cover"/>
							</div>
							
							<div class="p-4">
							
								<h3 class="text-lg font-semibold mb-2 text-card-foreground">
								  {item.name}
								</h3>
								<p class="text-muted-foreground mb-4 text-sm">{item.description}</p>
								<div class="flex items-center justify-between">
									<span class="text-xl font-bold text-restaurant-primary">
										${item.price}
									</span>
									<button class="bg-restaurant-primary text-restaurant-primary-foreground px-4 py-2 rounded-md hover:bg-restaurant-primary/90 transition-all">
									Add to Cart
									</button>
								</div>
								
							</div>
						  
						</div>
					{/each}
				{/each}
			{/if}
		</div>		
	</div>
</section>