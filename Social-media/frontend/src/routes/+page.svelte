<script lang="ts">
	import Postcard from "$lib/components/postcard.svelte"
	
	const posts = [
		{
			id: "1",
			author: {
			  name: "Sarah Chen",
			  username: "sarahchen",
			  avatar: "/src/lib/assets/default.jpeg"
			},
			content: "Just shipped a new feature! The feeling when everything works perfectly on the first try is unmatched 🚀\n\nBuilding in public has been such an incredible journey. The feedback from the community keeps me motivated!",
			createdAt: new Date(Date.now() - 1000 * 60 * 30), // 30 minutes ago
			likes: 124,
			reposts: 15,
			repliesCount: 28,
			isLiked: false,
			isReposted: false,
			image: "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=500&h=300&fit=crop"
		},
		{
			id: "2",
			author: {
			  name: "Sarah Chen",
			  username: "sarahchen",
			  avatar: "/src/lib/assets/default.jpeg"
			},
			content: "Just shipped a new feature! The feeling when everything works perfectly on the first try is unmatched 🚀\n\nBuilding in public has been such an incredible journey. The feedback from the community keeps me motivated!",
			createdAt: new Date(Date.now() - 1000 * 60 * 30), // 30 minutes ago
			likes: 124,
			reposts: 15,
			repliesCount: 28,
			isLiked: false,
			isReposted: false,
			image: "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=500&h=300&fit=crop"
		}
	]
</script>

<section class="p-2 max-w-2xl ml-4">
	<div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
		<h1 class="text-xl font-bold">Home</h1>
	</div>
	<div class="divide-y divide-border">
		{#each posts as post (post.id)}
			<Postcard {post} />
		{/each}
	</div>
</section>