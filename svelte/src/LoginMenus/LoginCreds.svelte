<script lang="ts">
    import { Button, Form, FormGroup, Label, Input } from 'sveltestrap';
    import { loginCompleted, loginSelectionChoice } from "../stores.js";
    import Cookies from 'js-cookie';
    import { loginFetch } from "../loginAlgo.js";

    let emsg: string = "";
    let processingSubmission: boolean = false;
    let formLoginUsername: string = "";
    let formLoginPassword: string = "";

    async function submitForm() {
        processingSubmission = true;
        const r = await loginFetch(formLoginUsername, formLoginPassword, false);
        switch (r[0]) {
            case 200:
                Cookies.set("nyn-user-tk", r[1], {expires:7});
                loginCompleted.set(true);
                break;
            case 403:
                emsg = "Username or password was incorrect.";
                break;
            case 500:
            default:
                emsg = "An unknown error occurred. Please try again later.";
                break;
        }
        processingSubmission = false;
    }
</script>

<main>
    <Form>
        <FormGroup>
            <Label for="form_login_username">Username</Label>
            <Input id="form_login_username" bind:value={formLoginUsername} />
        </FormGroup>
        <!-- TODO: forgot password link/view -->
        <FormGroup>
            <Label for="form_login_password">Password (<a on:click={() => loginSelectionChoice.set(3)} href="javascript:void(0);">forgot?</a>)</Label>
            <Input type="password" id="form_login_password" bind:value={formLoginPassword} />
        </FormGroup>
        <!-- TODO: toggle checkbox for keep-me-logged-in -->
        <!-- TODO: necessary code changes for above TODO -->
    </Form>
    <Button on:click={submitForm} disabled={processingSubmission}>Login</Button>
    <p>{emsg}</p>
</main>

<style>
</style>