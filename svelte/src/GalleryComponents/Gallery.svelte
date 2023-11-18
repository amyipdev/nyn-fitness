<script lang="ts">
    import type {GalleryWorkout} from "./GalleryWorkout.js";
    import GalleryItem from "./GalleryItem.svelte";
    import {Container, Row, Col} from "sveltestrap";
    export let wks: Array<GalleryWorkout>;
</script>

<main class="w-auto">
    <Container class="mx-auto px-1">
        <Row class="overflow-x-scroll flex-nowrap w-auto p-2 mx-auto align-items-stretch">
            {#each wks as wko}
                <Col class="nyn-galcol-color">
                    <div class="nyn-galcol-color h-100">
                        <GalleryItem wk={wko} />
                    </div>
                </Col>
            {/each}
        </Row>
    </Container>
</main>

<style>
    .nyn-galcol-color {
        background-color: #555533;
    }
</style>