<script lang="ts">
    import { Button } from 'sveltestrap';
    import { loginSelectionChoice } from "../stores.js";
</script>

<main>
    <Button color=danger on:click={() => loginSelectionChoice.set(1)} style="margin: 10px; width: 150px;">Sign In</Button>
    <br>
    <Button color=secondary on:click={() => loginSelectionChoice.set(2)} style="width: 150px;">Create Account</Button>
</main>

<style>
</style>