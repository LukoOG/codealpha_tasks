<script lang="ts">
	import { goto } from "$app/navigation";

	let { url, restaurant } = $props()
</script>

<div onclick={()=>goto(`restaurants/${restaurant.id}`)} class="bg-card rounded-lg overflow-hidden border border-border cursor-pointer transition-all hover:shadow-lg">
	<div class="aspect-video overflow-hidden">
		<img
		  src={url}
		  alt={restaurant.name}
		  class="w-full h-full object-cover transition-transform hover:scale-105"
		/>
	</div>
              
	<div class="p-6">
		<h3 class="text-xl font-semibold mb-2 text-card-foreground"> {restaurant.name} </h3>
		<p class="text-muted-foreground mb-4 line-clamp-2"> {restaurant.description} </p>

		<div class="flex items-center justify-between text-sm">
			<div class="flex items-center gap-1">
				<span class="text-restaurant-accent">⭐</span>
				<span class="font-medium text-card-foreground">{restaurant.avg_rating}</span>
			</div>
			
			<div class="text-muted-foreground">
				{restaurant.delivery_ime}
			</div>
			
			<div class="text-muted-foreground">
				${restaurant.delivery_fee} delivery
			</div>
			
		</div>

		<div className="mt-2">
			<span className="inline-block bg-secondary text-secondary-foreground px-2 py-1 rounded-full text-xs">
				{restaurant.cuisine}
			</span>
		</div>
		
	</div>
</div>