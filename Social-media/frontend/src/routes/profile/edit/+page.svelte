<script lang="ts">
	import { enhance } from "$app/forms";
	import { Label, Avatar } from "bits-ui";
	import Input from "$lib/components/ui/input.svelte";
	import Button from "$lib/components/ui/button.svelte";
	import Textarea from "$lib/components/ui/textarea.svelte"
	import { ArrowLeft } from "@lucide/svelte";
	import { invalidateAll } from "$app/navigation";
	
	import refreshAccessToken from "$lib/helpers/refreshAccessToken.ts"
	import { goto } from "$app/navigation";
	
	
	let { data } = $props()
	let { userData } = $derived(data)	
	
	let imageInput = $state()
	
	let previewUrl = $state<string|null>(userData.profile_pic);

	function handleFileChange(event: Event) {
		const file = (event.target as HTMLInputElement).files?.[0];
		if (file) {
			previewUrl = URL.createObjectURL(file);
		}
	}
	
	function goBack() {
		history.length > 1 ? history.back() : goto("/");
	}
	
	let disableBtn = $state<boolean>(false)
	const handleEnhance = () => {
		disableBtn = true
		
		return async ({ update, result }) => {
			await update()
			if(result.success){
				invalidateAll();
			}
			disableBtn = false
		}
	}
</script>

<section class="max-w-2xl mx-auto">
  <!-- Header -->
	<div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
	
		<div class="flex items-center gap-4">
			<Button onclick={goBack} variant="ghost" size="icon" class="rounded-full">
				<ArrowLeft class="h-5 w-5" />
			</Button>
			
			<div>
				<h1 class="text-xl font-bold">Edit profile</h1>
			</div>
			
		</div>
		
	</div>

	<!-- Form -->
	<form method="POST" action="?/update" use:enhance={handleEnhance} class="p-6">
	
		<div class="space-y-8">
			<!-- Avatar Section -->
			<div class="flex items-center gap-4">
				<Avatar.Root class="h-20 w-20">
					<Avatar.Image class="aspect-square h-full w-full" src={previewUrl} alt="swix {userData.username}" />
					<Avatar.Fallback class="flex h-full w-full items-center justify-center rounded-full bg-muted aspect-square text-2xl">A</Avatar.Fallback>
				</Avatar.Root>
				<input
					class="hidden"
					type="file"
					name="profile_pic"
					accept="image/*"
					bind:this={imageInput}
					onchange={handleFileChange}
				/>
				<Button onclick={()=>imageInput.click()} variant="outline" size="sm">
					Change photo
				</Button>
			</div>

			<!-- Form Fields -->
			<div class="space-y-4">
				<div class="space-y-2 grid grid-cols-2">
					<div class="gap-2 w-2/3">
						<Label.Root htmlFor="name">Firstname</Label.Root>
						<Input name="first_name" value={userData.first_name} id="name" placeholder="Your first name" />
						
					</div>
					<div class="gap-2 w-2/3">
						<Label.Root htmlFor="name">Lastname</Label.Root>
						<Input name="last_name" value={userData.last_name} id="name" placeholder="Your last name" />
						
					</div>
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="username">Username</Label.Root>
				  <Input
					id="username"
					placeholder="@username"
					name="username"
					value={userData.username}
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="bio">Bio</Label.Root>
				  <Textarea
					id="bio"
					placeholder="Tell people about yourself"
					class="min-h-[100px]"
					rows={4}
					value={userData.bio}
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="location">Location</Label.Root>
				  <Input
					id="location"
					name="location"
					value={userData.location}
					placeholder="Where are you located?"
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="website">Website</Label.Root>
				  <Input
					id="website"
					name="website"
					value={userData.website}
					placeholder="Your website URL"
				  />
				</div>
			</div>

			<!-- Action Buttons -->
			<div class="flex gap-4 pt-4">
				<Button onclick={()=>history.length > 1 ? history.back() : goto('/')} variant="outline" class="flex-1" >
					Cancel
				</Button>
				
				<Button disabled={disableBtn} type="submit" class="flex-1" >
					Save changes
				</Button>
			</div>
		  
		</div>
		
	</form>
</section>