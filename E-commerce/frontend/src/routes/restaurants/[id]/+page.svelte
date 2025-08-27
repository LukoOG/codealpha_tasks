<script lang='ts'>
  let { data } = $props()
</script>

<section class="min-h-screen bg-gradient-to-br from-orange-50 to-orange-100 p-6">
  <!-- Restaurant Header -->
  <div class="bg-white/80 backdrop-blur-md shadow-lg rounded-2xl p-6 mb-6">
    <div class="flex items-center gap-4">
      <img src={data.restaurant.logo} alt={data.restaurant.name} class="w-20 h-20 rounded-xl object-cover" />
      <div>
        <h1 class="text-2xl font-bold text-orange-600">{data.restaurant.name}</h1>
        <p class="text-sm text-gray-500">{data.restaurant.cuisine}</p>
        <div class="flex gap-4 text-sm text-gray-600">
          <span>⭐ {data.restaurant.rating}</span>
          <span>{data.restaurant.deliveryTime} mins</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Menu -->
  {#each data.menu as category}
    <div class="mb-8">
      <h2 class="text-xl font-semibold text-orange-600 mb-4">{category.name}</h2>
      <div class="space-y-4">
        {#each category.items as item}
          <div class="bg-white/80 backdrop-blur-md shadow rounded-xl p-4 flex justify-between items-center">
            <div>
              <h3 class="font-medium">{item.name}</h3>
              <p class="text-sm text-gray-500">{item.description}</p>
              <span class="text-orange-600 font-bold">${item.price}</span>
            </div>
            <button class="bg-orange-500 text-white px-3 py-1 rounded-xl hover:bg-orange-600">
              Add
            </button>
          </div>
        {/each}
      </div>
    </div>
  {/each}
</section>

<!-- Floating cart -->
<a
  href="/cart"
  class="fixed bottom-6 right-6 bg-orange-500 text-white px-6 py-3 rounded-2xl shadow-lg hover:bg-orange-600"
>
  View Cart (3)
</a>
