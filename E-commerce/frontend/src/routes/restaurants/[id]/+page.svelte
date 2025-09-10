<script lang='ts'>
	import { goto } from "$app/navigation";
	import { page } from "$app/state";
	import MenuCard from "$lib/components/restaurants/menuCard.svelte";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	
	let { data } = $props()
	let selectedCategory = $state("All")
	const categories = ["All"]
	
	let { restaurant } = data
	
	let menuPromise = fetch(`${PUBLIC_BACKEND_URL}/api/restaurants/${page.params.id}/`).then(res => res.json());
</script>
{#snippet CategoryFilters(category: string)}
	<button class={`px-4 py-2 rounded-full whitespace-nowrap transition-colors ${
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
			src={restaurant.image}
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
		  {#each categories as category}
			{@render CategoryFilters(category)}
		  {/each}
		</div>

		<!-- Menu Items -->
		<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each ['as'] as men}
				<MenuCard />
			{/each}
		</div>
	</div>
</section>