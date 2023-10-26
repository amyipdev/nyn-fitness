<script lang="ts">
    import { Styles, Button } from 'sveltestrap';
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
    loginSelectionChoice.subscribe((value) => {toggleView(value);});
</script>

<Styles />

<main>
    <h1>Login Page (navbar here)
    <!-- recommend to use a bootstrap icon - perhaps even without a background - for the back button -->
    <!-- should also be fixed position; NYN logo to the left, back to the right -->
    {#if currentView != 0}
        <Button on:click={() => toggleView(0)}>Back</Button>
    {/if}</h1>
    {#if viewportComponent == views[currentView]}
		<div id="viewport" on:outroend={updateViewportComponent} transition:fade>
			<svelte:component this={viewportComponent}></svelte:component>
		</div>
	{/if}
</main>

<style>
</style>