<script lang="ts">
    import { page } from "$app/state";
    import { goto } from "$app/navigation"

    import Login from "$lib/components/auth/login.svelte";
    import Register from "$lib/components/auth/register.svelte";

    const form = $derived(page.url.searchParams.get("form"))

    const updateAuthSearchParams = (value: string) => {
        const params = page.url.searchParams
        params.set("form", value)
        goto(`${page.url.pathname}?${params.toString()}`, { replaceState: true });
    }
</script>

<!-- snippetss -->
{#snippet changeFormBtn(form: String | null)}
    <p class="text-sm text-gray-600 text-center">
        {#if form == "login"}
            Don’t have an account? <a href="?form=register" onclick={()=>updateAuthSearchParams("register")} class="text-orange-500 hover:underline">Register</a>
        {:else if form == "register"}
            Already have an account? <a href="?form=login" onclick={()=>updateAuthSearchParams("login")} class="text-orange-500 hover:underline">Login</a>
        {/if}
    </p>
{/snippet}

<section class="min-h-screen flex items-center justify-center bg-gradient-to-br from-orange-50 to-orange-100">
  <div class="bg-white/80 backdrop-blur-md shadow-lg rounded-2xl p-8 w-full max-w-md">
    <h2 class="text-3xl font-bold mb-6 text-center text-orange-600">{form ? form.slice(0, 1).toUpperCase() + form.slice(1) : "Error"}</h2>

    <form method="POST" class="space-y-4">
        {#if form == "login"}
            <Login />
        {:else if form == "register"}
            <Register />
        {/if}
      {@render changeFormBtn(form)}
    </form>

  </div>
</section>