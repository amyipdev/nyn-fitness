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
    import type {GalleryWorkout} from "./GalleryWorkout.js";
    import GalleryItem from "./GalleryItem.svelte";
    import {Container, Row, Col} from "sveltestrap";
    export let wks: Array<GalleryWorkout>;
    export let galname: string;
</script>

<main class="w-auto">
    <Container class="mx-auto px-1">
        <Row><h2 class="nyn-gal-head" style="text-align: left;">{galname}</h2></Row>
        <div class="nyn-zz p-3">
            <Row class="overflow-x-scroll flex-nowrap w-auto p-2 mx-auto align-items-stretch">
                {#each wks as wko}
                    <Col class="">
                        <div class="nyn-galcol-color h-100" style="width: 250px;">
                            <GalleryItem wk={wko} />
                        </div>
                    </Col>
                {/each}
                <!-- Add "nothing here!" -->
            </Row>
        </div>
    </Container>
</main>

<style>
    .nyn-zz {
        min-height: 225px;
        background-color: #44444444;
    }
    .nyn-galcol-color {
        background-color: #77777777;
    }
    .nyn-gal-head {
        font-family: 'Open Sans', sans-serif;
        font-weight: 600;
    }
</style>