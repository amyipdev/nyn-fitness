<script lang="ts">
    import Cookies from 'js-cookie';
    import Gallery from "./GalleryComponents/Gallery.svelte";
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    let test: Array<GalleryWorkout> = [{wk_uuid:"Testdesc",wk_name:"TestName",descr:"This is a test description.",ytlink:"https://youtube.com/embed/XNatTFsuBBA",duration:"2:34"},
                                       {wk_uuid:"testwk",wk_name:"A Very Very Very Very Long Title",descr:"desc",ytlink:"",duration:"9:44"},
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