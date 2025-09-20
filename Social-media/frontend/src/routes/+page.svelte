<script lang="ts">
	import Postcard from "$lib/components/postcard.svelte";
	import ComposePost from "$lib/components/composePost.svelte";
	
	let { data } = $props()
	let { posts: p, user } = $derived(data)
	
	let posts = $state([...p]);
	
</script>

<section class="p-2 max-w-2xl ml-16">
	<div class="sticky top-0 z-10 bg-background/95 backdrop-blur border-b p-4">
		<h1 class="text-xl font-bold">Home</h1>
	</div>
	
	{#if user}
		<ComposePost addPost={(post)=>{console.log('adding');posts = [post, ...posts]}} {user} />
	{/if}
	
	<div class="divide-y divide-border">
		{#each posts as post (post.id)}
			<Postcard {post} />
		{/each}
	</div>
</section>