<script lang='ts'>
    let { data } = $props()
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
      <a
        href={`/restaurants/${restaurant.id}`}
        class="bg-white/80 backdrop-blur-md shadow-lg rounded-2xl p-4 hover:shadow-xl transition"
      >
        <img src={restaurant.image} alt={restaurant.name} class="rounded-xl w-full h-40 object-cover mb-4" />
        <h2 class="text-xl font-semibold text-orange-600">{restaurant.name}</h2>
        <p class="text-sm text-gray-500">{restaurant.cuisine}</p>
        <div class="flex justify-between mt-2 text-sm text-gray-600">
          <span>⭐ {restaurant.rating}</span>
          <span>{restaurant.deliveryTime} mins</span>
        </div>
      </a>
    {/each}
  </div>
</section>
