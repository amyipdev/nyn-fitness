<script lang="ts">
    import { Styles, Button } from 'sveltestrap';
    import {loginSelectionChoice} from "../stores.js";
</script>

<Styles />

<main>
    <Button color=secondary disabled>Create Account</Button>
    <br>
    <Button color=secondary on:click={function() {loginSelectionChoice.set(1);}}>Login</Button>
</main>

<style>
</style>