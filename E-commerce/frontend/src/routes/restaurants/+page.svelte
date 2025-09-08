<script lang='ts'>
	import RestaurantCard from "$lib/components/restaurants/restaurantCard.svelte";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	
    let { data } = $props()
	//console.log(data.restaurants)
</script>

<section class="min-h-screen bg-gradient-to-br from-orange-50 to-orange-100 p-6">
  <h1 class="text-3xl font-bold text-orange-600 mb-6">Restaurants</h1>

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
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each data.restaurants as restaurant}
		{@const url = PUBLIC_BACKEND_URL+restaurant.image}
		<RestaurantCard {url} {restaurant}/>
    {/each}
  </div>
</section>
