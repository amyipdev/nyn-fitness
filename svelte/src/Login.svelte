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
        <Container md>
            <h1><Image src="favicon.png" alt="Logo" style="height: 50px;" /><h1>NYN Fitness</h1></h1>

            <h3>
                {#if currentView != 0}
                    <Button on:click={() => loginSelectionChoice.set(0)}>Back</Button>
                {/if}
            </h3>

            {#if viewportComponent == views[currentView]}
                <div id="viewport" on:outroend={updateViewportComponent} transition:fade>
    	            <svelte:component this={viewportComponent}></svelte:component>
    		    </div>
    	    {/if}
        </Container>
    </div>

    <!--</Navbar>-->

</main>

<style>
    /*.nyn-divcent {
        transform: translateY(150%);
    }*/
    /*:global(body) {
        background: linear-gradient(180deg, #1b1848, #3a1848);
        margin: 0px;
        padding: 0px;
    }*/

    /*.bg-container {
        background: linear-gradient(to bottom, #493f82, #342b82);
        margin: 0px;
        padding: 200px;
    }*/
</style>