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