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
        <Button secondary on:click={() => switchHomeMode.set(1)}>Cancel</Button>
        <Button danger on:click={completeWorkout}>Done!</Button>
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