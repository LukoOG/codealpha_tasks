<script lang="ts">
	const item = {
		name: "TFC",
		image:"http://localhost:8000/media/products/Crispy_chicken.jpeg",
		description: "d",
		price: 3,
		
	}
</script>

<div class="bg-card rounded-lg overflow-hidden border border-border">
	<div class="aspect-video overflow-hidden">
		<img
		  src={item.image}
		  alt={item.name}
		  class="w-full h-full object-cover"
		/>
	</div>

	<div class="p-4">
		<h3 class="text-lg font-semibold mb-2 text-card-foreground">
		  {item.name}
		</h3>
		
		<p class="text-muted-foreground mb-4 text-sm">
		  {item.description}
		</p>

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