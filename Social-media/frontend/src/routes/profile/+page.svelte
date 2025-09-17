<script lang="ts">
	import Postcard from "$lib/components/postcard.svelte";
	import { Avatar, Tabs } from "bits-ui";
	import { MapPin, LinkIcon, Calendar } from "@lucide/svelte";
	import Button from "$lib/components/ui/button.svelte";
	
	let isFollowing = $state(false);
	
	const handleFollow = () => {}
	
	const userData = {
		name: "Alex Rivera",
		username: "alexdev",
		bio: "Full-stack developer passionate about creating beautiful, functional web applications. Always learning, always building.",
		location: "San Francisco, CA",
		website: "alexrivera.dev",
		joinedDate: "March 2020",
		following: 420,
		followers: 1248,
		posts: 342
	};
	
</script>

<section class="p-2 max-w-2xl ml-4">
      <!-- Header -->
      <div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
        <div>
          <h1 class="text-xl font-bold">{userData.name}</h1>
          <p class="text-sm text-muted-foreground">{userData.posts} posts</p>
        </div>
      </div>

      <!-- Profile Header -->
      <div class="p-6 border-b">
        <div class="flex items-start justify-between mb-4">
          <Avatar.Root class="h-24 w-24">
            <Avatar.Image class="aspect-square h-full w-full" src="/src/lib/assets/default.jpeg" />
            <Avatar.Fallback class="flex h-full w-full items-center justify-center rounded-full bg-muted aspect-square text-2xl">{userData.name[0]}</Avatar.Fallback>
          </Avatar.Root>
          
          <Button
            variant={isFollowing ? "outline" : "social"}
            onClick={handleFollow}
            class="px-6"
          >
            {isFollowing ? "Unfollow" : "Follow"}
          </Button>
        </div>

        <div class="space-y-3">
          <div>
            <h1 class="text-2xl font-bold">{userData.name}</h1>
            <p class="text-muted-foreground">@{userData.username}</p>
          </div>

          <p class="text-foreground">{userData.bio}</p>

          <div class="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
            <div class="flex items-center gap-1">
              <MapPin class="h-4 w-4" />
              <span>{userData.location}</span>
            </div>
            <div class="flex items-center gap-1">
              <LinkIcon class="h-4 w-4" />
              <a href={`https://${userData.website}`} class="text-social-blue hover:underline">
                {userData.website}
              </a>
            </div>
            <div class="flex items-center gap-1">
              <Calendar class="h-4 w-4" />
              <span>Joined {userData.joinedDate}</span>
            </div>
          </div>

          <div class="flex items-center gap-6 text-sm">
            <div>
              <span class="font-bold text-foreground">{userData.following}</span>
              <span class="text-muted-foreground ml-1">Following</span>
            </div>
            <div>
              <span class="font-bold text-foreground">{userData.followers}</span>
              <span class="text-muted-foreground ml-1">Followers</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Tabs -->
      <Tabs.Root defaultValue="posts" class="w-full">
        <Tabs.List class="grid w-full grid-cols-3 bg-transparent border-b rounded-none h-auto">
          <Tabs.Trigger value="posts" class="data-[state=active]:border-b-2 cursor-pointer data-[state=active]:border-social-blue rounded-none inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50">
            Posts
          </Tabs.Trigger>
          <Tabs.Trigger value="replies" class="data-[state=active]:border-b-2 cursor-pointer data-[state=active]:border-social-blue rounded-none inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50">
            Replies
          </Tabs.Trigger>
          <Tabs.Trigger value="likes" class="data-[state=active]:border-b-2 cursor-pointer data-[state=active]:border-social-blue rounded-none inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50">
            Likes
          </Tabs.Trigger>
        </Tabs.List>
        
        <Tabs.Content value="posts" class="mt-0">
          <p>stuff</p>
        </Tabs.Content>
        
        <Tabs.Content value="replies" class="mt-0">
          <div class="p-8 text-center text-muted-foreground">
            Replies coming soon!
          </div>
        </Tabs.Content>
        
        <Tabs.Content value="likes" class="mt-0">
          <div class="p-8 text-center text-muted-foreground">
            Liked posts coming soon!
          </div>
        </Tabs.Content>
      </Tabs.Root>
</section>