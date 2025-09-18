<script lang="ts">
	import { Calendar, MapPin, Smile, ImageIcon } from "@lucide/svelte"
	import Button from "$lib/components/ui/button.svelte"
</script>

<Card class="border-0 border-b rounded-none">
    <CardContent class="p-4">
        <div class="flex space-x-3">
          <Avatar class="h-12 w-12">
            <AvatarImage src="/placeholder-avatar.jpg" />
            <AvatarFallback>YU</AvatarFallback>
          </Avatar>
          
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
					{content.length > 0 && (
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
						{isNearLimit && (
						  <span class={`text-sm ${isOverLimit ? 'text-destructive' : 'text-yellow-600'}`}>
							{remainingChars}
						  </span>
						)}
					  </div>
					)}
					
					<Button 
					  variant="social" 
					  size="sm"
					  onClick={handlePost}
					  disabled={!content.trim() || isOverLimit}
					  class="px-6"
					>
					  Post
					</Button>
				  </div>
				</div>
			</div>
        </div>
	</CardContent>
</Card>