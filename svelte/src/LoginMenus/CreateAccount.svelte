<script lang="ts">
    import { Styles, Form, FormGroup, Label, Input, Button } from "sveltestrap";
    import { loginCompleted } from "../stores.js";
    import { loginFetch } from "../loginAlgo.js";
    import Cookies from 'js-cookie';

    let emsg: string = "";
    let formCreateUsn: string = "";
    let formCreatePwd: string = "";
    let formCreateDn: string = "";
    let processingSubmission: boolean = false;
    
    async function submitForm() {
        processingSubmission = true;
        const r = await fetch("/api/create_account", {
            method: "POST",
            body: JSON.stringify({
                usn: formCreateUsn,
                dn: formCreateDn,
                pwd: formCreatePwd
            }),
            headers: {
                "Content-Type": "application/json"
            }
        });
        switch (r.status) {
            case 200:
                const rs = await loginFetch(formCreateUsn, formCreatePwd, false);
                if (rs[0] != 200) {
                    emsg = "A problem occurred."
                    break;
                }
                Cookies.set("nyn-user-tk", rs[1], {expires:7})
                loginCompleted.set(true);
                break;
            case 500:
            default:
                emsg = "An error occurred. Try another username."
                break;
        }
        processingSubmission = false;
    }
</script>

<Styles />

<main>
    <Form>
        <FormGroup>
            <Label for="form_create_usn">Username</Label>
            <Input id="form_create_usn" bind:value={formCreateUsn} />
        </FormGroup>
        <FormGroup>
            <Label for="form_create_dn">Display Name</Label>
            <Input id="form_create_dn" bind:value={formCreateDn} />
        </FormGroup>
        <FormGroup>
            <Label for="form_create_pwd">Password</Label>
            <Input type="password" id="form_create_pwd" bind:value={formCreatePwd} />
        </FormGroup>
    </Form>
    <Button on:click={submitForm} disabled={processingSubmission}>Create Account</Button>
    <p>{emsg}</p>
</main>

<style>
</style>