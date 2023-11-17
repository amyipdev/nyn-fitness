<script lang="ts">
    import type {GalleryWorkout} from "./GalleryWorkout.js";
    import GalleryItem from "./GalleryItem.svelte";
    import {Container} from "sveltestrap";
    export let wks: Array<GalleryWorkout>;
</script>

<main class="nyn-gallery-color w-auto">
    <Container class="mx-auto px-1">
        <div class="nyn-scrollable row overflow-x-scroll flex-nowrap w-auto p-2 mx-auto">
            {#each wks as wko}
                <div class="col">
                    <GalleryItem wk={wko} />
                </div>
            {/each}
        </div>
    </Container>
</main>

<style>
    .nyn-scrollable {
        /*overflow-x: scroll;
        white-space: nowrap;*/
    }
    .nyn-gallery-color {
        background-color: #aa3333;
    }
</style>