<script lang="ts">
	import { page } from "$app/state";
	import { PUBLIC_BACKEND_URL } from "$env/static/public"
	
	let { cart, user } = page.data
	
	let containerRef;
	console.log(!!cart)
	
	let cartItems = $state<[]>([])
	for(const c of cart){
		for(const i of c.items){
			cartItems.push(i)
		}
	}
	$inspect(cartItems[0])
</script>
{#if cart.length <= 0}
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
								<p class="text-restaurant-primary font-bold">${item.product.price}</p>
							</div>

							<div class="flex items-center gap-3">
								<button 
									class="w-8 h-8 rounded-full bg-secondary text-secondary-foreground flex items-center justify-center hover:bg-secondary/80" 
									onclick={() => handleQuantityChange(item.id, item.quantity - 1)}
								>
								-
								</button>
								
								<span class="w-8 text-center font-medium text-card-foreground">
									{item.quantity}
								</span>
								
								<button
									class="w-8 h-8 rounded-full bg-secondary text-secondary-foreground flex items-center justify-center hover:bg-secondary/80"
									onclick={() => handleQuantityChange(item.id, item.quantity + 1)}
								>
								+
								</button>
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
						$34<!--${getTotalPrice().toFixed(2)}-->
					</span>
					</div>

					<div class="flex gap-4">
					<button class="flex-1 bg-secondary text-secondary-foreground py-3 rounded-md hover:bg-secondary/80 transition-colors" onclick={clearCart}>
						Clear Cart
					</button>
					<button class="flex-1 bg-restaurant-primary text-restaurant-primary-foreground py-3 rounded-md hover:bg-restaurant-primary/90 transition-colors">
						Checkout
					</button>
				</div>
			</div>
		</div>
	</section>
{/if}
