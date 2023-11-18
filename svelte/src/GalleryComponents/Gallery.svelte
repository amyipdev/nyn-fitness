<script lang="ts">
    import type {GalleryWorkout} from "./GalleryWorkout.js";
    import GalleryItem from "./GalleryItem.svelte";
    import {Container, Row, Col} from "sveltestrap";
    export let wks: Array<GalleryWorkout>;
    export let galname: string;
</script>

<main class="w-auto">
    <Container class="mx-auto px-1">
        <Row><h2 style="text-align: left;">{galname}</h2></Row>
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
        background-color: #444444;
    }
    .nyn-galcol-color {
        background-color: #555533;
    }
</style>