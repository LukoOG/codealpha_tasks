<script lang="ts">
	import { Plus, House, User, Mail } from "@lucide/svelte";
	import { page } from "$app/state";
	
	let collapsed = $state(false);
	let showCreatePost = $state(false);
	
	let navigationItems = [
		{ title: "Home", url: "/", icon: House },
		{ title: "Messages", url: "/messages", icon: Mail },
		{ title: "Profile", url: "/profile", icon: User },
	];
	
	function getNavCls(isActive: boolean) {
		return isActive ? "bg-sidebar-accent text-sidebar-accent-foreground" : "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground";
	}
	
	//console.log(page.url.pathname)
</script>

<!-- Sidebar container -->
<section class="border-r fixed top-0 left-0 min-h-full flex flex-col bg-sidebar-background text-sidebar-foreground {collapsed ? "w-14" : "w-64"}">
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
</section>
