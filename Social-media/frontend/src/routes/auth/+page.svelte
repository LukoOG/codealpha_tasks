<script lang="ts">
    import { page } from "$app/state";
    import { goto } from "$app/navigation";
    import { enhance } from '$app/forms';
    import type { PageProps } from "./$types.js";
	import { X, Eye, EyeOff } from "@lucide/svelte";
	import { Label } from "bits-ui";
	
	import Button from "$lib/components/ui/button.svelte";
    import Login from "$lib/components/auth/login.svelte";
    import Register from "$lib/components/auth/register.svelte";

    let { form }: PageProps = $props()
	
	let isLogin = $state<boolean>(true)
	$inspect(isLogin)
	
	let showPassword = $state(true)
</script>

<!-- snippetss -->
{#snippet changeFormBtn(form: String | null)}
    <p class="text-sm text-gray-600 text-center">
        {#if form == "login"}
            Don’t have an account? <a href={undefined} onclick={()=>updateAuthSearchParams("register")} class="text-orange-500 cursor-pointer hover:underline">Register</a>
        {:else if form == "register"}
            Already have an account? <a href={undefined} onclick={()=>updateAuthSearchParams("login")} class="text-orange-500 cursor-pointer hover:underline">Login</a>
        {/if}
    </p>
{/snippet}

<!-- main html body -->
<div class="min-h-screen flex items-center justify-center bg-background px-4">
	<div class="w-full max-w-md space-y-8">
		<!-- Header -->
		<div class="text-center">
			<h1 class="text-3xl font-bold text-foreground">SocialApp</h1>
			<p class="mt-2 text-muted-foreground">
				{isLogin ? "Welcome back" : "Join the conversation"}
			</p>
		</div>

		<!-- Form Container -->
		<div class="bg-card border border-border rounded-lg p-6 shadow-sm">
			<!-- Toggle Buttons -->
			<div class="flex mb-6 p-1 bg-muted rounded-lg">
				<Button variant={isLogin ? "default" : "ghost"} class="flex-1" onclick={() => {isLogin = !isLogin}}>
					Sign In
				</Button>
				<Button variant={!isLogin ? "default" : "ghost"} class="flex-1" onclick={() => {isLogin = !isLogin}}>
					Sign Up
				</Button>
			</div>

			<!-- Forms -->
			{#if isLogin}
				<Login />
			{:else if !isLogin}
				<Register />
			{/if}
		</div>

		<!-- Footer -->
		<div class="text-center text-sm text-muted-foreground">
			<p>{isLogin ? "Don't have an account? " : "Already have an account? "}
				<button onClick={() => setIsLogin(!isLogin)} class="text-primary hover:underline font-medium">
					{isLogin ? "Sign up" : "Sign in"}
				</button>
			</p>
		</div>
	</div>
</div>