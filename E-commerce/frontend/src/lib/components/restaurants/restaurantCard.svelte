<script lang="ts">
	let { url, restaurant } = $props()
	console.log(url)
</script>
<a
href={`/restaurants/${restaurant.id}`}
class="bg-white/80 backdrop-blur-md shadow-lg rounded-2xl p-4 hover:shadow-xl transition"
>
	<img src={url} alt={restaurant.name} class="rounded-xl w-full h-40 object-cover mb-4" />
	<h2 class="text-xl font-semibold text-orange-600">{restaurant.name}</h2>
	<p class="text-sm text-gray-500">{restaurant.cuisine}</p>
	<div class="flex justify-between mt-2 text-sm text-gray-600">
	  <span>⭐ {restaurant.rating}</span>
	  <span>{restaurant.deliveryTime} mins</span>
	</div>
</a>