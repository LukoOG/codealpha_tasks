<script lang='ts'>
	import RestaurantCard from "$lib/components/restaurants/restaurantCard.svelte";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	
    let { data } = $props()
	//console.log(data.restaurants)
</script>

<section class="min-h-screen bg-background px-6 py-8">
	<div class="max-w-7xl mx-auto">
		<h1 class="text-4xl font-bold text-center mb-8 text-foreground">Choose Your Restaurant</h1>

		<!-- Filter + Search -->
		<div class="flex items-center gap-4 mb-6">
			<input
			  type="text"
			  placeholder="Search restaurants..."
			  class="flex-1 rounded-xl border border-orange-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
			/>
			<select class="rounded-xl border border-orange-200 px-3 py-2">
			  <option>All cuisines</option>
			  <option>Burgers</option>
			  <option>Pizza</option>
			  <option>Chinese</option>
			</select>
		</div>

		<!-- Restaurant grid -->
		<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each data.restaurants as restaurant}
				{@const url = "http://localhost:8000/media/banner.jpg"}
				<RestaurantCard {url} {restaurant}/>
			{/each}
		</div>
	</div>
</section>
