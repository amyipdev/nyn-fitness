<script lang="ts">
    import Cookies from 'js-cookie';
    import Gallery from "./GalleryComponents/Gallery.svelte";
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    let test: Array<GalleryWorkout> = [{wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""},
                                       {wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""}];
</script>

<main>
    <h1>Home Page</h1>
    <Gallery wks={test} />
</main>

<style>
</style>