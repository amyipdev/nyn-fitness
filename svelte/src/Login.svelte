<script lang="ts">
    import { Styles } from 'sveltestrap';
    import SelectionView from "./LoginMenus/Selection.svelte";
    import LoginCredsView from "./LoginMenus/LoginCreds.svelte";
    import CreateAccountView from "./LoginMenus/CreateAccount.svelte";
    import { fade } from 'svelte/transition';
    import { SvelteComponent } from 'svelte';
    import { loginSelectionChoice } from "./stores.js";

    const views = [SelectionView, LoginCredsView, CreateAccountView];

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
    <h1>Login Page (navbar here)</h1>
    {#if viewportComponent == views[currentView]}
		<div id="viewport" on:outroend={updateViewportComponent} transition:fade>
			<svelte:component this={viewportComponent}></svelte:component>
		</div>
	{/if}
</main>

<style>
</style>