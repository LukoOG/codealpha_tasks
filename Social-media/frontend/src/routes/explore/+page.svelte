<script lang="ts">
	import { Avatar } from "bits-ui";
	import { Users, MapPin } from "@lucide/svelte";
	import Button from "$lib/components/ui/button.svelte";
	import { goto } from "$app/navigation";
	
	let { data } = $props()
	let { profiles } = data
	console.log(profiles)
	
	const handleProfileClick = (username: string) => {
		goto(`/profile/${username}`)
	}
</script>

<section class="max-w-2xl mx-auto">
	<div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
		<h1 class="text-xl font-bold">Explore</h1>
		<p class="text-sm text-muted-foreground">Discover new people</p>
	</div>

	<div class="divide-y">
		{#each profiles as profile (profile.id)}
			<div class="rounded-lg border bg-card text-card-foreground shadow-sm border-0 border-b rounded-none cursor-pointer hover:bg-muted/50 transition-colors" 
			onclick={() => handleProfileClick(profile.username)}>
				<div class="p-6 pt-0 p-4">
					<div class="flex items-start justify-between">
						<div class="flex items-start gap-3 flex-1">
							<Avatar.Root class="h-12 w-12">
								<Avatar.Image src={profile.profile_pic} />
								<Avatar.Fallback class="flex h-full w-full items-center justify-center rounded-full bg-muted aspect-square text-2xl">{profile.name[0]}</Avatar.Fallback>
							</Avatar.Root>

							<div class="flex-1 min-w-0">
								<div class="flex items-center gap-2">
									<h3 class="font-semibold text-foreground truncate">
									{profile.name}
									</h3>
									<span class="text-muted-foreground">@{profile.username}</span>
									</div>

									<p class="text-sm text-foreground mt-1 line-clamp-2">
									{profile.bio}
									</p>

									<div class="flex items-center gap-4 mt-2 text-xs text-muted-foreground">
									<div class="flex items-center gap-1">
									<MapPin class="h-3 w-3" />
									<span>{profile.location}</span>
									</div>
									<div class="flex items-center gap-1">
									<Users class="h-3 w-3" />
									<span>{profile.followers} followers</span>
									</div>
								</div>
							</div>
						</div>

						<Button variant="outline" size="sm" class="ml-4">
						View
						</Button>
					</div>
				</div>
			</div>
		{/each}
	</div>
</section>