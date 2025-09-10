<script lang="ts">
    import { goto } from "$app/navigation";
	import { page } from "$app/state";
    
    let { user } = $props()
    let authenticated = $state<boolean>(false)

    if (user){
        authenticated = true
    }

    const updateSearchParams = (query: "login" | "register") => {
        const param = new URLSearchParams({form_state: query})
        return goto(`auth?${param.toString()}`)
    }
	
	console.log(page)

    // test
    const logout = async () =>{
        const res = await fetch("http://127.0.0.1:8000/api/auth/logout", { method: "POST"})
        if (res.ok){
            return true
        }
        return false
    }
</script>

{#snippet actions()}
    <div class='actions'>
        {#if !authenticated}
            <button onclick={()=>{updateSearchParams("login")}}>Login</button>
            <button onclick={()=>{updateSearchParams("register")}}>Register</button>
        {:else if authenticated}
            <button onclick={logout}>Logout</button>
        {/if}
    </div>
{/snippet}

<nav class="nav-wrapper">
	<div class="max-w-7xl mx-auto flex items-center justify-between">
		<div class="text-2xl font-bold text-restaurant-primary cursor-pointer">
			Svellit
		</div>
		
		<button aria-current={page.url.pathname === '/' ? "page" : ""} class="" onclick={() => goto('/')}>
            Home
         </button>
		 
		 <button aria-current={page.url.pathname === '/restaurants' ? "page" : ""} class="" onclick={() => goto('/restaurants')}>
            Restaurants
         </button>
		
		<div class="flex items-center gap-6">
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