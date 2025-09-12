<script lang="ts">
	let { disable } = $props()
	console.log(disable)
</script>

<div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input id="email" name="email" type="email" required
        class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-400 focus:outline-none"/>
</div>

<div>
    <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
    <input id="password" name="password" type="password" required
        class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-400 focus:outline-none"/>
</div>
{#if disable}
	<button type="button" disabled
		class="w-full bg-none text-white py-2 rounded-lg font-semibold flex items-center justify-center cursor-not-allowed">
		<!-- Simple spinner -->
		<svg class="animate-spin h-8 w-8 text-black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
			<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
			<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
		</svg>
	</button>
{:else if !disable}
	<button type="submit" class="w-full bg-orange-500 cursor-pointer text-white py-2 rounded-lg font-semibold hover:bg-orange-600 transition">
		Sign In
	</button>
{/if}
