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
    import { Container, Row, Col } from "sveltestrap";
    import {currentWorkout,switchHomeMode} from '../stores.js';
    export let wk: GalleryWorkout;
</script>

<main>
    <!-- todo: make <a> into onclick, load workouts -->
    <div on:click={() => {currentWorkout.set(wk);switchHomeMode.set(3);}}>
        <Container fluid class="p-2">
            <Row>
                <Col><img class="img-fluid" alt="Thumbnail" src={`https://i.ytimg.com/vi/${wk[3].slice(-11)}/maxresdefault.jpg`}></Col>
            </Row>
            <Row class="w-100">
                <Col xs="9"><p class="text-start text-truncate fw-bold">{wk[1]}</p></Col>
                <Col xs="3"><p class="text-end fst-italic fst-semibold">{wk[4]}</p></Col>
            </Row>
            <Row>
                <Col><p class="text-start text-truncate">{wk[2]}</p></Col>
            </Row>
        </Container>
    </div>
</main>

<style>
</style>