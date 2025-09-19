<script lang="ts">
	import { Calendar, MapPin, Smile, ImageIcon } from "@lucide/svelte"
	import Button from "$lib/components/ui/button.svelte"
	import Textarea from "$lib/components/ui/textarea.svelte"
	import Input from "$lib/components/ui/input.svelte"
	
	import { Avatar } from "bits-ui";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	
	let { user } = $props()
	
	let isOverLimit =$state(false)
	let isNearLimit =$state(false)
	let content =$state("asa")
	
	const maxChars = 100
</script>

<section class="rounded-lg border bg-card text-card-foreground shadow-sm border-0 border-b rounded-none">
  <div class="p-6 pt-0 p-4">
    <div class="flex space-x-3">
          <Avatar.Root class="h-24 w-24">
            <Avatar.Image class="aspect-square h-full w-full" src="{PUBLIC_BACKEND_URL}/{user.media}" />
            <Avatar.Fallback class="flex h-12 w-12 items-center justify-center rounded-full bg-muted aspect-square">{user.username[0].toUpperCase()}</Avatar.Fallback>
          </Avatar.Root>

      <div class="flex-1 space-y-4">
        <Textarea
          placeholder="What's happening?"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          class="border-0 resize-none text-xl placeholder:text-muted-foreground focus-visible:ring-0 p-0 min-h-[60px]"
          style={{ boxShadow: 'none' }}
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
                    <path
                      class="stroke-current text-muted-foreground/20"
                      strokeWidth="3"
                      fill="none"
                      d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                    <path
                      class={`stroke-current ${isOverLimit ? 'text-destructive' : isNearLimit ? 'text-yellow-500' : 'text-social-blue'}`}
                      strokeWidth="3"
                      fill="none"
                      strokeDasharray={`${Math.min((content.length / maxChars) * 100, 100)}, 100`}
                      d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                  </svg>
                </div>
                {#if isNearLimit}
                  <span class={`text-sm ${isOverLimit ? 'text-destructive' : 'text-yellow-600'}`}>
                    2
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
