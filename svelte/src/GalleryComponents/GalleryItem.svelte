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