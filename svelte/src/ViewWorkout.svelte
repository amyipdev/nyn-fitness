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
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    import {currentWorkout,switchHomeMode} from './stores.js';
    import {Button} from 'sveltestrap';
    import Cookies from 'js-cookie';

    async function completeWorkout() {
        const r = await fetch("/api/complete_workout", {
            method: "POST",
            body: JSON.stringify({
                tk: Cookies.get("nyn-user-tk"),
                wk_uuid: $currentWorkout[0]
            }),
            headers: {
                "Content-Type": "application/json"
            }
        });
        if (r.status != 200) {
            console.log("Workout completion not set");
            alert("NOTE: Workout progress not saved, you've done this workout before!");
        }
        switchHomeMode.set(1);
    }
</script>

<main>
    <h1 class="text-truncate text-center w-75 mx-auto os600 text-light">{$currentWorkout[1]}</h1>
    <p class="text-center w-75 mx-auto os600">{$currentWorkout[2]}</p>
    <iframe title="YouTube" src={$currentWorkout[3]} frameborder="0" allowfullscreen allow="fullscreen; autoplay; web-share; picture-in-picture;"></iframe>
    <div>
        <Button on:click={() => switchHomeMode.set(1)}>Cancel</Button>
        <Button on:click={completeWorkout}>Done!</Button>
    </div>
</main>

<style>
    .os600 {
        font-family: "Open Sans", sans-serif;
        font-weight: 600;
    }
    iframe {
        aspect-ratio: 16 / 9 !important;
        max-height: 50vh;
        height: 100%;
        max-width: 600px;
        width: 95%;
    }
</style>