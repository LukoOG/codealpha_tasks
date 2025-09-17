<script lang="ts">
	import { Label, Avatar } from "bits-ui";
	import Input from "$lib/components/ui/input.svelte";
	import Button from "$lib/components/ui/button.svelte";
	import Textarea from "$lib/components/ui/textarea.svelte"
	import { ArrowLeft } from "@lucide/svelte";
	
</script>

<section class="max-w-2xl mx-auto">
  <!-- Header -->
	<div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
	
		<div class="flex items-center gap-4">
			<Button variant="ghost" size="icon" className="rounded-full">
				<ArrowLeft class="h-5 w-5" />
			</Button>
			
			<div>
				<h1 class="text-xl font-bold">Edit profile</h1>
			</div>
			
		</div>
		
	</div>

	<!-- Form -->
	<div class="p-6">
	
		<div class="space-y-8">
			<!-- Avatar Section -->
			<div class="flex items-center gap-4">
				<Avatar.Root class="h-20 w-20">
					<Avatar.Image class="aspect-square h-full w-full" src="" />
					<Avatar.Fallback class="flex h-full w-full items-center justify-center rounded-full bg-muted aspect-square text-2xl">A</Avatar.Fallback>
				</Avatar.Root>
				<Button variant="outline" size="sm">
					Change photo
				</Button>
			</div>

			<!-- Form Fields -->
			<div class="space-y-4">
				<div class="space-y-2">
					<Label.Root htmlFor="name">Name</Label.Root>
					<Input
					id="name"
					placeholder="Your display name"
					/>
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="username">Username</Label.Root>
				  <Input
					id="username"
					placeholder="@username"
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="bio">Bio</Label.Root>
				  <Textarea
					id="bio"
					placeholder="Tell people about yourself"
					className="min-h-[100px]"
					rows={4}
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="location">Location</Label.Root>
				  <Input
					id="location"
					placeholder="Where are you located?"
				  />
				</div>

				<div class="space-y-2">
				  <Label.Root htmlFor="website">Website</Label.Root>
				  <Input
					id="website"
					placeholder="Your website URL"
				  />
				</div>
			</div>

			<!-- Action Buttons -->
			<div class="flex gap-4 pt-4">
				<Button variant="outline" className="flex-1" >
					Cancel
				</Button>
				
				<Button className="flex-1" >
					Save changes
				</Button>
			</div>
		  
		</div>
		
	</div>
</section>