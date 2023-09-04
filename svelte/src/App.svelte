<script lang="ts">
	import { Styles, Button } from 'sveltestrap';
	import { fade } from 'svelte/transition';
	import { SvelteComponent } from 'svelte';
	import LoginView from './Login.svelte';
	import HomeView from './Home.svelte';
	import LoadingView from './Loading.svelte';
	export let name;

	const views = [LoginView, HomeView, LoadingView];

	let viewportComponent: SvelteComponent = null;
	let currentView: integer = 2;

	function toggleView(nv: integer) {
		currentView = nv;
	}

	function updateViewportComponent() {
		viewportComponent = views[currentView];
	}
	updateViewportComponent();
</script>

<Styles />

<main>
	{#if viewportComponent == views[currentView]}
		<div id="viewport" on:outroend={updateViewportComponent} transition:fade>
			<svelte:component this={viewportComponent}></svelte:component>
		</div>
	{/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
