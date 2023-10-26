<script lang="ts">
	import { Styles } from 'sveltestrap';
	import { fade } from 'svelte/transition';
	import { SvelteComponent } from 'svelte';
	import LoginView from './Login.svelte';
	import HomeView from './Home.svelte';
	import LoadingView from './Loading.svelte';
	import Cookies from 'js-cookie';
	import {loginCompleted} from "./stores.js";
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

	function handleLogin() {
		toggleView(0);

		//loginCompleted.subscribe(() => {console.log("hhh"); toggleView(1)});
	}
	$: $loginCompleted && toggleView(1);

	setTimeout(async function() {
		let usr_tk: string = Cookies.get("nyn-user-tk");
		if (usr_tk != undefined) {
			console.log(usr_tk);
			const tk_f = await fetch("/api/verify_token?" + new URLSearchParams({tk: usr_tk}));
			const tk_fr = await tk_f.json();
			tk_fr["status"] ? toggleView(1) : handleLogin();
		} else {
			console.log(usr_tk);
			handleLogin();
		}

	}, 1250);
</script>

<Styles />

<svelte:head>
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
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}*/
	/*
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}*/
</style>
