<script lang="ts">
    import { goto } from "$app/navigation";
	import { page } from "$app/state";
	
	import { logout } from "$lib/helpers/auth.ts"
    
    let { user } = $props()
    let authenticated = $state<boolean>(false)

    if (user){
        authenticated = true
    }

    const updateSearchParams = (query: "login" | "register") => {
        const param = new URLSearchParams({form_state: query})
        return goto(`auth?${param.toString()}`)
    }
</script>

{#snippet actions()}
    <div class='actions'>
        {#if !authenticated}
            <button onclick={()=>{updateSearchParams("login")}}>Login</button>
            <button onclick={()=>{updateSearchParams("register")}}>Register</button>
        {:else if authenticated}
			<button class="px-4 py-2 rounded-md transition-colors relative" aria-current={page.url.pathname === '/cart' ? "page" : ""} onclick={()=>goto('/cart')}>
				Cart
				<span class="absolute -top-2 -right-2 bg-restaurant-accent text-restaurant-primary-foreground text-xs rounded-full h-5 w-5 flex items-center justify-center">
                6
              </span>
			</button>
            <button onclick={logout}>Logout</button>
        {/if}
    </div>
{/snippet}

<nav class="nav-wrapper">
	<div class="max-w-7xl mx-auto flex items-center justify-between">
		<div class="text-2xl font-bold text-restaurant-primary cursor-pointer">
			Svellit
		</div>
		

		
		<div class="flex items-center gap-6">
			<button aria-current={page.url.pathname === '/' ? "page" : ""} class="" onclick={() => goto('/')}>
				Home
			 </button>
			 
			 <button aria-current={page.url.pathname === '/restaurants' ? "page" : ""} class="" onclick={() => goto('/restaurants')}>
				Restaurants
			 </button>
			{@render actions()}
		</div>
	</div>
 </nav>

<style>
	button{
		color: var(--color-foreground);
		padding: 0.5rem 1rem;
		cursor: pointer;
		border-radius: 0.375rem;
		&[aria-current="page"]{
			color: var(--color-restaurant-primary-foreground);
			background: var(--color-restaurant-primary);
		}
		
		&:not([aria-current="page"]):hover{
			color: var(--color-restaurant-primary);
		}
	}
</style>