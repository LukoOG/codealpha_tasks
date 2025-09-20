<script lang="ts">
	import { PUBLIC_BACKEND_URL } from "$env/static/public";

	import { Plus, House, User, Mail, Search } from "@lucide/svelte";
	import { page } from "$app/state";
	import { goto } from "$app/navigation";
	
	import Button from "$lib/components/ui/button.svelte"
	
	let collapsed = $state(false);
	let showCreatePost = $state(false);
	
	let navigationItems = [
		{ title: "Home", url: "/", icon: House },
		{ title: "Messages", url: "/messages", icon: Mail },
		{ title: "Explore", url: "/explore", icon: Search },
	];
	
	let { user } = $props();
	let isAuthenticated = $derived.by(()=>user ? true : false)
	
	function getNavCls(isActive: boolean) {
		return isActive ? "bg-sidebar-accent text-sidebar-accent-foreground" : "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground";
	}
	
	const logout = 	async () => {
		try {
			await fetch('/api/logout', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' }
			});

			goto('/', { invalidateAll: true });
		} catch (error) {
			console.error('Logout failed', error);
		}
	}
</script>
{#snippet actions()}
	<div class="absolute bottom-2 p-2 m-2 w-[90%]">
		{#if isAuthenticated}
			<!-- User profile button -->
			<a
				href="/profile/{user.username}"
				class="flex items-center space-x-3 p-3 hover:bg-secondary rounded-lg transition-all duration-200"
			>
				<img
					src="{PUBLIC_BACKEND_URL}/{user.avatar}"
					alt="Profile"
					class="h-10 w-10 rounded-full object-cover"
				/>
				<span class="text-lg font-medium">@{user.username}</span>
			</a>
			
			<Button
				onclick={logout}
				class="mt-5 flex items-center justify-center p-3 bg-primary text-primary-foreground rounded-lg font-medium hover:bg-primary/90 transition-all duration-200"
			>
				Log out
			</Button>
		{:else}
			<!-- Login button -->
			<a
				href="/auth"
				class="flex items-center justify-center p-3 bg-primary text-primary-foreground rounded-lg font-medium hover:bg-primary/90 transition-all duration-200"
			>
				Log in
			</a>
		{/if}
	</div>
{/snippet}

<!-- Sidebar container -->
<section class="border-r fixed sticky top-0 left-0 max-h-screen flex flex-col bg-sidebar-background text-sidebar-foreground {collapsed ? "w-14" : "w-64"}">
	<div class="p-4">
		<div class="mb-8">
			{#if !collapsed}
				<h1 class="text-3xl font-bold ml-6 text-primary">Swix</h1>
			{/if}
		</div>

		<!-- Navigation -->
		<div class="p-2">
			<ul class="flex w-full flex-col justify-between gap-2">
				{#each navigationItems as item}
					{@const Icon = item.icon}
					<li class="relative">
						<a href={item.url} class="flex items-center space-x-3 p-3 hover:bg-secondary rounded-lg transition-all duration-200">
							<Icon class="h-4 w-4" />
							{#if !collapsed}
								<span class="text-lg">{item.title}</span>
							{/if}
						</a>
					</li>
				{/each}
			</ul>
		</div> 	
	</div>
	{@render actions()}
</section>
