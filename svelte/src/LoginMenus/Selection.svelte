<script lang="ts">
    import { Button } from 'sveltestrap';
    import { loginSelectionChoice } from "../stores.js";
</script>

<main>
    <Button color=secondary on:click={() => loginSelectionChoice.set(2)}>Create Account</Button>
    <br>
    <Button color=secondary on:click={() => loginSelectionChoice.set(1)}>Login</Button>
</main>

<style>
</style>