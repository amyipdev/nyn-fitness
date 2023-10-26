<script lang="ts">
    import { Styles, Button } from 'sveltestrap';
    import SelectionView from "./LoginMenus/Selection.svelte";
    import LoginCredsView from "./LoginMenus/LoginCreds.svelte";
    import { fade } from 'svelte/transition';
    import { SvelteComponent } from 'svelte';
    import { loginSelectionChoice } from "./stores.js";

    const views = [SelectionView, LoginCredsView];

    let viewportComponent: SvelteComponent = null;
	let currentView: integer = 0;

	function toggleView(nv: integer) {
        currentView = nv;
    }

	function updateViewportComponent() {
        viewportComponent = views[currentView];
    }
	updateViewportComponent();
    loginSelectionChoice.subscribe((value) => {toggleView(value);})

    //export let loginCompleted = false;
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