<script lang="ts">
    import type {GalleryWorkout} from "./GalleryWorkout.js";
    import { Container, Row, Col } from "sveltestrap";
    export let wk: GalleryWorkout;
</script>

<main class="nyn-galleryitem-color">
    <a>
        <Container fluid class="p-2">
            <Row>
                <Col><img class="img-fluid" alt="Thumbnail" src={`https://i.ytimg.com/vi/${wk.ytlink.slice(-11)}/maxresdefault.jpg`}></Col>
            </Row>
            <Row class="w-100">
                <Col xs="9"><p class="text-start text-truncate fw-bold">{wk.wk_name}</p></Col>
                <Col xs="3"><p class="text-end fst-italic fst-semibold">{wk.duration}</p></Col>
            </Row>
            <Row>
                <Col><p class="text-start text-truncate">{wk.descr}</p></Col>
            </Row>
        </Container>
    </a>
</main>

<style>
    .nyn-galleryitem-color {
        width: 250px;
    }
</style>