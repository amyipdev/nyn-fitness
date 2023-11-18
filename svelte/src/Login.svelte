<script lang="ts">
    import { Styles, Button, Image, Container } from 'sveltestrap';
    import SelectionView from "./LoginMenus/Selection.svelte";
    import LoginCredsView from "./LoginMenus/LoginCreds.svelte";
    import CreateAccountView from "./LoginMenus/CreateAccount.svelte";
    import ForgotPasswordView from "./LoginMenus/ForgotPassword.svelte";
    import { fade } from 'svelte/transition';
    import { SvelteComponent } from 'svelte';
    import { loginSelectionChoice } from "./stores.js";

    const views = [SelectionView, LoginCredsView, CreateAccountView, ForgotPasswordView];

    let viewportComponent: SvelteComponent | null = null;
	let currentView: number = 0;

	function toggleView(nv: number) {
        currentView = nv;
    }

	function updateViewportComponent() {
        viewportComponent = views[currentView];
    }
	updateViewportComponent();
    loginSelectionChoice.subscribe((value) => toggleView(value));
</script>

<main>
    <!--Login Page (navbar here) -->
    <!-- recommend to use a bootstrap icon - perhaps even without a background - for the back button -->
    <!-- should also be fixed position; NYN logo to the left, back to the right -->
    <!--<Navbar color="dark" dark>-->
    <div class="nyn-divcent mx-auto">
        <Container>
            <img id="nyn-logo-img" src="favicon.png" alt="Logo" on:click={() => loginSelectionChoice.set(0)}>
            <h1 class="text-light" id="nyn-login-text-brand" on:click={() => loginSelectionChoice.set(0)}>NYN Fitness</h1>

            {#if viewportComponent == views[currentView]}
                <div id="viewport" on:outroend={updateViewportComponent} transition:fade>
                    <div class="nyn-login-switch mx-auto">
    	               <svelte:component this={viewportComponent}></svelte:component>
                    </div>
    		    </div>
    	    {/if}
        </Container>
    </div>

    <!--</Navbar>-->

</main>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
    .nyn-divcent {
        display: flex;
        align-items: center;
        height: 90vh;
    }
    .nyn-login-switch {
        max-width: 400px;
    }
    #nyn-login-text-brand {
        font-size: 2rem;
        text-decoration: none;
        font-weight: 700;
        font-family: 'Open Sans', sans-serif;
        transition: font-size 0.5s;
    }
    #nyn-login-text-brand:hover {
        font-size: 2.2rem;
        text-decoration: underline;
    }
    #nyn-logo-img {
        height: 84px;
        transition: height 0.5s;
    }
    #nyn-logo-img:hover {
        height: 96px;
    }
</style>