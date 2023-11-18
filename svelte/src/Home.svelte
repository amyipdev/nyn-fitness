<script lang="ts">
    import Cookies from 'js-cookie';
    import Gallery from "./GalleryComponents/Gallery.svelte";
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    
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
        console.log(dat);
        loaded = true;
    }
    setValues();
</script>

<main>
    <h1>Home Page</h1>
    {#if loaded}
        {#each dat as gal, index}
            <!--<h2 style="text-align: left;">{names[index]}</h2>-->
            <Gallery wks={gal} galname={names[index]} />
        {/each}
    {/if}
</main>

<style>
</style>