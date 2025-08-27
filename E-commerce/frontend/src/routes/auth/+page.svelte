<script lang="ts">
    import { page } from "$app/state";
    import { goto } from "$app/navigation";
    import { enhance } from '$app/forms';
    import type { PageProps } from "./$types.js";

    import Login from "$lib/components/auth/login.svelte";
    import Register from "$lib/components/auth/register.svelte";

    let { form }: PageProps = $props()
    const form_state = $derived(page.url.searchParams.get("form_state"))

    const updateAuthSearchParams = (value: string) => {
        const params = page.url.searchParams
        params.set("form_state", value)
        goto(`${page.url.pathname}?${params.toString()}`, { replaceState: true });
    }
</script>

<!-- snippetss -->
{#snippet changeFormBtn(form: String | null)}
    <p class="text-sm text-gray-600 text-center">
        {#if form == "login"}
            Don’t have an account? <a href={undefined} onclick={()=>updateAuthSearchParams("register")} class="text-orange-500 hover:underline">Register</a>
        {:else if form == "register"}
            Already have an account? <a href={undefined} onclick={()=>updateAuthSearchParams("login")} class="text-orange-500 hover:underline">Login</a>
        {/if}
    </p>
{/snippet}

<!-- main html body -->
<section class="min-h-screen flex items-center justify-center bg-gradient-to-br from-orange-50 to-orange-100">
  <div class="bg-white/80 backdrop-blur-md shadow-lg rounded-2xl p-8 w-full max-w-md">
    <h2 class="text-3xl font-bold mb-6 text-center text-orange-600">{form_state ? form_state.slice(0, 1).toUpperCase() + form_state.slice(1) : ""}</h2>

    <form method="POST" action="?/{form_state}" class="space-y-4" use:enhance>
        <input type="hidden" name="action" value={form_state} />
        {#if form_state == "login"}
            <Login />
        {:else if form_state == "register"}
            <Register />
                <!-- {:else}
        thro error -->
        {/if}
      {@render changeFormBtn(form_state)}
    </form>
    {#if form?.error}
        <p>{ form.error.detail }</p>
    {/if}

  </div>
</section>