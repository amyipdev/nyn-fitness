<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<!--
nyn-fitness: the dynamic recommendation fitness app
Copyright (C) 2023 Amy Parker <amy@amyip.net>
				   Kevin Ramirez <thekevinramirez@csu.fullerton.edu>
				   Nicholas Goulart <nick.goulart@csu.fullerton.edu>
				   Theresa Nguyen <ttnguyen1011@csu.fullerton.edu>
				   Dat Lam <Dlam42@csu.fullerton.edu>
				   Srinidhi Chevvuri <srinidhi.chevvuri@csu.fullerton.edu>

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA or visit the
GNU Project at https://gnu.org/licenses. The GNU Affero General Public
License version 3 is available at, for your convenience,
https://www.gnu.org/licenses/agpl-3.0.en.html.
-->

<script lang="ts">
	import { Styles } from 'sveltestrap';
	import { fade } from 'svelte/transition';
	import { SvelteComponent } from 'svelte';
	import LoginView from './Login.svelte';
	import HomeView from './Home.svelte';
	import LoadingView from './Loading.svelte';
	import ViewWorkout from './ViewWorkout.svelte';
	import SettingsView from './Settings.svelte'
	import Cookies from 'js-cookie';
	import { loginCompleted, switchHomeMode } from "./stores.js";
	export let name: string;

	const views = [LoginView, HomeView, LoadingView, ViewWorkout, SettingsView];

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
	$: $switchHomeMode == 0 && toggleView(0);
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
        background: linear-gradient(180deg, #1b1848, #3a1848) no-repeat fixed;
        margin: 0;
        padding: 0;
    }
</style>
