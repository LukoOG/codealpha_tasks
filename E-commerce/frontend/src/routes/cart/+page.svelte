<script lang="ts">
	import { page } from "$app/state";
	import { enhance } from "$app/forms"
	import { PUBLIC_BACKEND_URL } from "$env/static/public"
	import { cartItemsCount} from "$lib/global/cache.svelte.ts";
	
	let { cart, user } = page.data
	
	
	let containerRef = $state()
	
	let cartItems = $state<[]>([])
	for(const c of cart){
		for(const i of c.items){
			cartItems.push(i)
		}
	}
	//cartCache.create(cart)
	//console.log(cart)
	
	const getTotalPrice = () => {
		return cartItems.reduce((t, curr)=>t + curr.total_price, 0)
	}
	
	const getTotalItems = () => {
		return cartItems.reduce((t, curr)=>t + curr.quantity, 0)
	}
	
	//accessible to navbar
	cartItemsCount.change(getTotalItems())
	
	const handleQuantityChange = (id:number, amount:number) => {
		cartItems = cartItems.map((item)=>{
			if(item.id === id){
				item.quantity = amount
			}
			return item
		}).filter((item)=>item.quantity > 0)
		/*
		cartItems = cartItems.map((item)=>{
			if(item.id === id && amount > 0){
				item.quantity = amount
			}
			return item
		}).filter((item)=>item.quantity > 0)
		*/
		cartItemsCount.change(getTotalItems())
	}
	
	const handleRemoveItem = (id:number, e: Event) => {
		cartItems = cartItems.filter((item)=>item.id != id)
	}
	
	const clearCart = () => {
		cartItems = []
	}
</script>
{#if cartItems.length <= 0}
	<div class="min-h-screen bg-background flex items-center justify-center">
		<div class="text-center">
			<h1 class="text-3xl font-bold text-foreground mb-4">Your Cart is Empty</h1>
			<p class="text-muted-foreground">Add some delicious items to get started!</p>
		</div>
	</div>
{:else}
	<section class="min-h-screen bg-background px-6 py-8">
		<div class="max-w-4xl mx-auto">
			<h1 class="text-4xl font-bold text-center mb-8 text-foreground">
				Your Cart
			</h1>

			<div bind:this={containerRef} class="space-y-4 mb-8">
				{#each cartItems as item}
					{@const url = `${PUBLIC_BACKEND_URL}/${item.product.image}`}
						<div class="cart-item bg-card rounded-lg p-6 border border-border flex items-center gap-4">
							<img src={url} alt={item.name} class="w-20 h-20 object-cover rounded-md"/>

							<div class="flex-1">
								<h3 class="text-lg font-semibold text-card-foreground">{item.product.name}</h3>
								<p class="text-muted-foreground text-sm">{item.product.description}</p>
								<p class="text-restaurant-primary font-bold">${item.total_price}</p>
							</div>

							<div class="flex items-center gap-3">
								<form method="POST" action="?/sync" use:enhance>
									<input class="hidden" name ="id" value={item.id}>
									<input class="hidden" name ="quantity" value={item.quantity -1}>
									<button 
										class="w-8 h-8 rounded-full bg-secondary text-secondary-foreground flex items-center justify-center hover:bg-secondary/80" 
										onclick={() => handleQuantityChange(item.id, item.quantity - 1)}
									>
									-
									</button>
								</form>
								
								<span class="w-8 text-center font-medium text-card-foreground">
									{item.quantity}
								</span>
								
								<form method="POST" action="?/sync" use:enhance>
									<input class="hidden" name ="id" value={item.id}>
									<input class="hidden" name ="quantity" value={item.quantity +1}>
									<button
										class="w-8 h-8 rounded-full bg-secondary text-secondary-foreground flex items-center justify-center hover:bg-secondary/80"
										onclick={() => handleQuantityChange(item.id, item.quantity + 1)}
									>
									+
									</button>
								</form>
							</div>
							
							<button class="text-destructive hover:text-destructive/80 ml-4" onclick={(e) => handleRemoveItem(item.id, e)}>
								Remove
							</button>
						</div>
				{/each}
			</div>

			<!-- Total and Checkout -->
			<div class="bg-card rounded-lg p-6 border border-border">
				<div class="flex justify-between items-center mb-4">
					<span class="text-xl font-semibold text-card-foreground">Total:</span>
					<span class="text-2xl font-bold text-restaurant-primary">
						${getTotalPrice().toFixed(2)}
					</span>
					</div>

					<div class="flex gap-4">
					<button class="cursor-pointer flex-1 bg-secondary text-secondary-foreground py-3 rounded-md hover:bg-destructive/80 transition-colors" onclick={clearCart}>
						Clear Cart
					</button>
					<button class="cursor-pointer flex-1 bg-restaurant-primary text-restaurant-primary-foreground py-3 rounded-md hover:bg-restaurant-primary/90 transition-colors">
						Checkout
					</button>
				</div>
			</div>
		</div>
	</section>
{/if}
