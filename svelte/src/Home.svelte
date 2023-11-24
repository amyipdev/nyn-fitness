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
    import Cookies from 'js-cookie';
    import Gallery from "./GalleryComponents/Gallery.svelte";
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    import {Container,Row,Col} from "sveltestrap";
    import {switchHomeMode} from "./stores.js";

    const CNT: number = 10;

    let usr_tk: string = Cookies.get("nyn-user-tk");
    const endpoints = [
        "/api/recommendations/fyp?" + new URLSearchParams({tk: usr_tk, cnt: CNT}),
        "/api/recommendations/general?" + new URLSearchParams({tk: usr_tk, cnt: CNT, catid: 0}),
        "/api/recommendations/general?" + new URLSearchParams({tk: usr_tk, cnt: CNT, catid: 1}),
        "/api/recommendations/general?" + new URLSearchParams({tk: usr_tk, cnt: CNT, catid: 2}),
        "/api/recommendations/recent?" + new URLSearchParams({tk: usr_tk, cnt: CNT})
    ];
    const names = [
        "For You",
        "Cardio",
        "Core",
        "HIIT",
        "Recent"
    ];
    let dat: Array<Array<GalleryWorkout>> = [];
    let loaded = false;
    async function setValues() {
        const requests = endpoints.map((uri) => fetch(uri));
        const responses = await Promise.all(requests);
        const jsons = responses.map((resp) => resp.json());
        const ldat = await Promise.all(jsons);
        ldat.forEach((d) => dat.push(d));
        loaded = true;
    }
    setValues();
</script>

<main>
    <div class="my-2">
        <Container>
            <Row>
                <div class="d-flex justify-content-between">
                    <Col xs="4">
                        <div class="d-flex align-items-center">
                            <img id="nyn-logo-img" src="favicon.png" alt="Logo">
                            <h1 id="nyn-logo-home-txt" class="text-light">&nbsp;&nbsp;&nbsp;NYN Fitness</h1>
                        </div>
                    </Col>
                    <div class="d-flex align-items-center justify-content-end me-5">
                        <Col xs="2">
                            <i on:click={() => switchHomeMode.set(4)} id="nyn-settings-button" class="bi bi-gear-fill"/>
                        </Col>
                    </div>
                </div>
            </Row>
        </Container>
    </div>
    <br />
    {#if loaded}
        {#each dat as gal, index}
            <!--<h2 style="text-align: left;">{names[index]}</h2>-->
            <Gallery wks={gal} galname={names[index]} />
            <br />
        {/each}
    {/if}
</main>

<style>
    @media (max-width: 425px) {
        #nyn-logo-home-txt {
            display: none;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 426px) and (max-width: 767px) {
        #nyn-logo-home-txt {
            font-size: 0.8rem !important;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 768px) and (max-width: 989px) {
        #nyn-logo-home-txt {
            font-size: 1.2rem !important;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 990px) and (max-width: 1199px) {
        #nyn-logo-home-txt {
            font-size: 1.8rem !important;
        }
        #nyn-logo-img {
            height: 48px !important;
        }
    }
    #nyn-logo-img {
        height: 64px;
    }
    #nyn-logo-home-txt {
        font-size: 2.8rem;
        text-decoration: none;
        font-weight: 700;
        font-family: 'Open Sans', sans-serif;
    }
    #nyn-settings-button {
        font-size: 1.3rem;
        transition: font-size 0.4s;
    }
    #nyn-settings-button:hover {
        font-size: 1.8rem;
    }
</style>