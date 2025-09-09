<script lang="ts">
	import { page } from "$app/state"
	import { goto } from "$app/navigation";
</script>   
	
<section class="min-h-screen bg-background">
	<!-- Hero Section -->
	
  <div class="relative bg-gradient-to-br from-restaurant-primary to-restaurant-secondary text-restaurant-primary-foreground">
	<div class="max-w-7xl mx-auto px-6 py-24">
	  <div class="text-center">
		<h1 class="text-5xl md:text-6xl font-bold mb-6">
		  Delicious Food
		  <span class="block text-restaurant-accent">Delivered Fast</span>
		</h1>
		<p class="text-xl mb-8 max-w-2xl mx-auto opacity-90">
		  Discover amazing restaurants near you and get your favorite meals delivered right to your door
		</p>
		<button
		  class="bg-restaurant-primary-foreground text-restaurant-primary px-8 cursor-pointer py-4 rounded-lg text-lg font-semibold hover:bg-opacity-90 transition-all transform hover:scale-105" data-sveltekit-preload-data="hover"
		  onclick={() => goto('/restaurants')}
		>
		  Explore Restaurants
		</button>
	  </div>
	</div>
  </div>

	<!-- Featured Products Section -->
	<!-- Direcly lik eACH ON ETO A RETAURAN T -->
	<div class="featured mt-16 flex flex-row justify-between mx-auto px-6 max-w-6xl">
		<div class="bg-white rounded-2xl shadow-md p-16	 text-center">
			<img src="https://picsum.dev//static/12/200" alt="Pizza" class="rounded-xl mx-auto mb-4"/>
			<h3 class="text-xl font-semibold">Pizza</h3>
			<p class="text-gray-500">Cheesy, hot & delicious</p>
		</div>
		
		<div class="bg-white rounded-2xl shadow-md p-16 text-center">
			<img src="https://picsum.dev//static/163/200" alt="Burger" class="rounded-xl mx-auto mb-4"/>
			<h3 class="text-xl font-semibold">Burgers</h3>
			<p class="text-gray-500">Juicy grilled perfection</p>
		</div>
		
		<div class="bg-white rounded-2xl shadow-md p-16 text-center">
			<img src="https://picsum.dev//static/123/200" alt="Sushi" class="rounded-xl mx-auto mb-4"/>
			<h3 class="text-xl font-semibold">Sushi</h3>
			<p class="text-gray-500">Fresh & healthy rolls</p>
		</div>
	</div>
	
	<div class="max-w-7xl mx-auto px-6 py-16">
	
		<h2 class="text-3xl font-bold text-center mb-12 text-foreground">Why Choose Svellit?</h2>
		<div class="grid md:grid-cols-3 gap-8">
			<div class="text-center p-6 bg-card rounded-lg border border-border">
				<div class="w-16 h-16 bg-restaurant-primary rounded-full flex items-center justify-center mx-auto mb-4">
					<span class="text-2xl">🚀</span>
				</div>
				<h3 class="text-xl font-semibold mb-2 text-card-foreground">Fast Delivery</h3>
				<p class="text-muted-foreground">Get your food delivered in 30 minutes or less</p>
			</div>
	  
			<div class="text-center p-6 bg-card rounded-lg border border-border">
				<div class="w-16 h-16 bg-restaurant-secondary rounded-full flex items-center justify-center mx-auto mb-4">
				  <span class="text-2xl">⭐</span>
				</div>
				<h3 class="text-xl font-semibold mb-2 text-card-foreground">Quality Food</h3>
				<p class="text-muted-foreground">Fresh ingredients from top-rated restaurants</p>
			</div>
	  
			<div class="text-center p-6 bg-card rounded-lg border border-border">
				<div class="w-16 h-16 bg-restaurant-accent rounded-full flex items-center justify-center mx-auto mb-4">
					<span class="text-2xl">💳</span>
				</div>
				<h3 class="text-xl font-semibold mb-2 text-card-foreground">Easy Payment</h3>
				<p class="text-muted-foreground">Secure and convenient payment options</p>
			</div>
			
		</div>
	</div>
</section>

<style>
	.featured{
		div:hover{
			box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
			translate: 3px -3px;
			border: 1px solid oklch(98.4% 0.003 247.858);
			transition: 0.2s ease-in;
		}
	}
</style>