<script lang="ts">
    import { Styles, Button, Form, FormGroup, Label, Input } from 'sveltestrap';
    import {loginCompleted} from "../stores.js";
    import Cookies from 'js-cookie';
    let emsg = "";
    let processingSubmission = false;
    let formLoginUsername = "";
    let formLoginPassword = "";
    async function submitForm() {
        processingSubmission = true;
        const r = await fetch("/api/generate_token", {
            method: "POST",
            body: JSON.stringify({
                usn: formLoginUsername,
                pwd: formLoginPassword,
                long: false
            }),
            headers: {
                "Content-Type": "application/json"
            }
        });
        console.log(r.status);
        switch (r.status) {
            case 200:
                const rj = await r.json();
                Cookies.set("nyn-user-tk", rj["token"], {expires:7});
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

<Styles />

<main>
    <Form>
        <FormGroup>
            <Label for="username">Username</Label>
            <Input id="form_login_username" bind:value={formLoginUsername} />
        </FormGroup>
        <!-- TODO: forgot password link/view -->
        <FormGroup>
            <Label for="password">Password</Label>
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