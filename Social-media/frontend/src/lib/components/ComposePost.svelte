<script lang="ts">
	import { Calendar, MapPin, Smile, ImageIcon } from "@lucide/svelte"
	import Button from "$lib/components/ui/button.svelte"
	import Textarea from "$lib/components/ui/textarea.svelte"
	import Input from "$lib/components/ui/input.svelte"
	
	import { Avatar } from "bits-ui";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	
	let { user } = $props()
	
	const maxChars = 100
	let content =$state("")
	const remainingChars = $derived(maxChars - content.length)
	let isOverLimit =$derived(remainingChars < 0)
	let isNearLimit =$derived(remainingChars <= 20)
	let progress = $derived(Math.min((content.length / maxChars) * 100, 100))
</script>

<section class="rounded-lg border bg-card text-card-foreground shadow-sm border-0 border-b rounded-none">
  <div class="p-6">
    <div class="flex space-x-3">
          <Avatar.Root class="relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full">
            <Avatar.Image class="aspect-square h-full w-full" src="{PUBLIC_BACKEND_URL}/{user.avatar}" />
            <Avatar.Fallback class="flex h-12 w-12 items-center justify-center rounded-full bg-muted aspect-square">{user.username[0].toUpperCase()}</Avatar.Fallback>
          </Avatar.Root>

      <div class="flex-1 space-y-4">
        <Textarea
          placeholder="What's happening?"
          bind:value={content}
          class="border-0 resize-none text-xl placeholder:text-muted-foreground focus-visible:ring-0 p-0 min-h-[60px]"
          style="box-shadow: none;"
        />

        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <Button variant="ghost" size="icon" class="h-9 w-9 text-social-blue hover:bg-social-blue/10">
              <ImageIcon class="h-5 w-5" />
            </Button>
            <Button variant="ghost" size="icon" class="h-9 w-9 text-social-blue hover:bg-social-blue/10">
              <MapPin class="h-5 w-5" />
            </Button>
            <Button variant="ghost" size="icon" class="h-9 w-9 text-social-blue hover:bg-social-blue/10">
              <Smile class="h-5 w-5" />
            </Button>
            <Button variant="ghost" size="icon" class="h-9 w-9 text-social-blue hover:bg-social-blue/10">
              <Calendar class="h-5 w-5" />
            </Button>
          </div>

          <div class="flex items-center space-x-3">
            {#if true}
              <div class="flex items-center space-x-2">
				<div class="relative w-8 h-8">
				  <svg class="w-8 h-8 transform -rotate-90" viewBox="0 0 36 36">
					<!-- Background circle -->
					<path
					  class="stroke-current text-muted-foreground/20"
					  stroke-width="4"
					  fill="none"
					  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
					/>
					<!-- Progress circle -->
					<path
					  class="stroke-current"
					  class:text-destructive={isOverLimit}
					  class:text-yellow-500={isNearLimit && !isOverLimit}
					  class:text-social-blue={!isNearLimit && !isOverLimit}
					  stroke-width="4"
					  fill="none"
					  stroke-dasharray="{progress}, 100"
					  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
					/>
				  </svg>
				</div>
                {#if isNearLimit}
                  <span class="text-sm {isOverLimit ? 'text-destructive' : 'text-yellow-600'}">
                    {remainingChars}
                  </span>
                {/if}
              </div>
            {/if}

            <Button 
              variant="social" 
              size="sm"
              disabled={!content.trim() || isOverLimit}
              class="px-6"
            >
              Post
            </Button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
