<script lang="ts">
	import { Styles } from 'sveltestrap';
	import { fade } from 'svelte/transition';
	import { SvelteComponent } from 'svelte';
	import LoginView from './Login.svelte';
	import HomeView from './Home.svelte';
	import LoadingView from './Loading.svelte';
	import ViewWorkout from './ViewWorkout.svelte'
	import Cookies from 'js-cookie';
	import { loginCompleted, switchHomeMode } from "./stores.js";
	export let name: string;

	const views = [LoginView, HomeView, LoadingView, ViewWorkout];

	let viewportComponent: SvelteComponent | null = null;
	let currentView: number = 2;

	function toggleView(nv: number) {
		currentView = nv;
	}

	function updateViewportComponent() {
		viewportComponent = views[currentView];
	}
	updateViewportComponent();

	setTimeout(async function() {
		let usr_tk: string | undefined = Cookies.get("nyn-user-tk");
		if (usr_tk != undefined) {
			const tk_f = await fetch("/api/verify_token?" + new URLSearchParams({tk: usr_tk}));
			const tk_fr = await tk_f.json();
			toggleView(tk_fr["status"] ? 1 : 0);
		} else {
			toggleView(0);
		}
	}, 1250);
	// TODO: evaluate turning this into a .subscribe inside a handleLogin() function
	$: $loginCompleted && toggleView(1);
	$: $switchHomeMode && toggleView($switchHomeMode);
</script>

<Styles />

<svelte:head>
	<!-- @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap'); -->
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@600;700&display=swap" rel="stylesheet"> 
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap" rel="stylesheet">
	<title>{name}</title>
</svelte:head>

<main>
	{#if viewportComponent == views[currentView]}
		<div id="viewport" on:outroend={updateViewportComponent} transition:fade>
			<svelte:component this={viewportComponent}></svelte:component>
		</div>
	{/if}
</main>
<!-- TODO: better dynamic resizing -->
<style>
	main {
		text-align: center;
		padding: 1em;
		/*max-width: 320px;*/
		margin: 0 auto;
	}
	/*
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}*/
	:global(body) {
		height: 100%;
        background: linear-gradient(180deg, #1b1848, #3a1848);
		background-repeat: no-repeat;
		background-attachment: fixed;
        margin: 0px;
        padding: 0px;
    }
</style>
