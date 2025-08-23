<script lang="ts">
    import Navbar from "../lib/components/navbar.svelte";
	import { page } from "$app/state"
    let user = page.data.user
</script>

<div>
    <section class="">
        <Navbar { user } />
    </section>
    <section class="min-h-screen flex flex-col items-center justify-center">
        <div class="text-center max-w-2xl px-4">
            <h1 class="text-5xl font-extrabold text-gray-900 mb-4">
            Delicious Meals, Delivered Fast 🍕
            </h1>
            <p class="text-lg text-gray-600 mb-6">
            Explore a wide variety of meals from top restaurants near you. Fresh, tasty, and just a click away.
            </p>
            <a href="/products" class="px-6 py-3 bg-orange-500 text-white rounded-xl shadow hover:bg-orange-600 transition">
            Browse Menu
            </a>
        </div>

        <!-- Featured Products Section -->
        <div class="mt-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 px-6 max-w-6xl">
            <div class="bg-white rounded-2xl shadow-md p-6 text-center">
            <img src="https://source.unsplash.com/200x200/?pizza" alt="Pizza" class="rounded-xl mx-auto mb-4"/>
            <h3 class="text-xl font-semibold">Pizza</h3>
            <p class="text-gray-500">Cheesy, hot & delicious</p>
            </div>
            <div class="bg-white rounded-2xl shadow-md p-6 text-center">
            <img src="https://source.unsplash.com/200x200/?burger" alt="Burger" class="rounded-xl mx-auto mb-4"/>
            <h3 class="text-xl font-semibold">Burgers</h3>
            <p class="text-gray-500">Juicy grilled perfection</p>
            </div>
            <div class="bg-white rounded-2xl shadow-md p-6 text-center">
            <img src="https://source.unsplash.com/200x200/?sushi" alt="Sushi" class="rounded-xl mx-auto mb-4"/>
            <h3 class="text-xl font-semibold">Sushi</h3>
            <p class="text-gray-500">Fresh & healthy rolls</p>
            </div>
        </div>
    </section>
</div>