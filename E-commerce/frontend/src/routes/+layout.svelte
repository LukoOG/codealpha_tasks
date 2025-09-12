<script lang="ts">
    import Navbar from "../lib/components/navbar.svelte";
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { page } from "$app/state";

	let { children } = $props();
	
	
    let user = $derived(page.data.user)
	let authPage = $derived.by(()=>{
		if(page.route.id === "/auth"){
			return true
		} else {
			return false
		}
	})
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Svellit</title>
</svelte:head>

{#snippet renderNavbar()}
	{#if !authPage}
		<Navbar { user } />
	{/if}
{/snippet}

<div>
	{@render renderNavbar()}
	{@render children?.()}
</div>

