<script lang="ts">
    import { goto } from "$app/navigation"
    let authenticated = $state<boolean>(false)

    const updateSearchParams = (query: "login" | "register") => {
        const param = new URLSearchParams({form: query})
        return goto(`auth?${param.toString()}`)
    }
</script>

{#snippet actions()}
    <div class='actions'>
        {#if authenticated}
            <button onclick={()=>{updateSearchParams("login")}}>Login</button>
            <button onclick={()=>{updateSearchParams("register")}}>Register</button>
        {:else if !authenticated}
            <button onclick={()=>{console.log('logout'); authenticated = !authenticated}}>Logout</button>
        {/if}
    </div>
{/snippet}

<section class="nav-container">
    <nav class="nav-wrapper">
        <p>Logo</p>
        <div>
            Svellit
        </div>
        {@render actions()}
    </nav>
</section>

<style>
    .actions{
        justify-content: space-between;

        button{
            background: blue;
            padding: 8px 16px;
            border-radius: 16px;
            transition: ease-out 0.5s;
        }

        button:hover{
            background: red;
        }
    }
</style>