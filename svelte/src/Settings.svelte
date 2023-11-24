<script lang="ts">
    import {Button} from "sveltestrap";
    import {switchHomeMode,loginCompleted,loginSelectionChoice} from "./stores.js";
    import Cookies from "js-cookie";
    // all values should be submitted as one list [v0,v1,...]
    // later, use this list (user_uuid concat on end) for mysql
    async function handleSettingsSubmission() {
        let vec = [box0c];
        for (let i = 1; i < 16; ++i) {
            vec.push(document.getElementById(`nyn-settings-${i}`).value);
        }
        vec.push(Cookies.get("nyn-user-tk"));
        const r = await fetch("/api/settings/set", {
            method: "POST",
            body: JSON.stringify(vec),
            headers: {
                "Content-Type": "application/json"
            }
        });
        if (r.status != 200) {
            console.log("Settings save failure");
            alert("Settings not saved, an error occurred!");
        }
        switchHomeMode.set(1);
    }
    let box0c: number = 0;
    async function setSliderValues() {
        let usr_tk = Cookies.get("nyn-user-tk");
        let vect_rs = await fetch("/api/settings/get?" + new URLSearchParams({tk: usr_tk}));
        let vect = await vect_rs.json();
        box0c = vect[0];
        for (let i = 1; i < 16; ++i) {
            document.getElementById(`nyn-settings-${i}`).value = vect[i];
        }
    }
    setSliderValues();
    function logOut() {
        Cookies.remove("nyn-user-tk");
        loginCompleted.set(false);
        loginSelectionChoice.set(0);
        switchHomeMode.set(0);
    }
</script>

<main>
    <h1 id="nyn-settings-title">Settings</h1>
    <br />
    <div id="nyn-form-box" class="mx-auto">
        <p>Experience level</p>
        <div class="d-flex justify-content-between">
            <div>
                <Button color=light outline={box0c != -6} on:click={() => box0c = -6} class="rounded-circle"><i class="bi bi-stars nyn-fs-xem"></i></Button>
                <p class="nyn-exp-text">Beginner</p>
            </div>
            <div>
                <Button color=light outline={box0c != -3} on:click={() => box0c = -3} class="rounded-circle"><i class="bi bi-star nyn-fs-xem"></i></Button>
                <p class="nyn-exp-text">Novice</p>
            </div>    
            <div>    
                <Button color=light outline={box0c != 0} on:click={() => box0c = 0} class="rounded-circle"><i class="bi bi-star-half nyn-fs-xem"></i></Button>
                <p class="nyn-exp-text">Intermediate</p>
            </div>
            <div>    
                <Button color=light outline={box0c != 3} on:click={() => box0c = 3} class="rounded-circle"><i class="bi bi-star-fill nyn-fs-xem"></i></Button>
                <p class="nyn-exp-text">Advanced</p>
            </div>
            <div>    
                <Button color=light outline={box0c != 6} on:click={() => box0c = 6} class="rounded-circle"><i class="bi bi-moon-stars-fill nyn-fs-xem"></i></Button>
                <p class="nyn-exp-text">Pro</p>
            </div>    
        </div>
        <br />
        <label for="nyn-settings-1" class="form-label">Duration preference</label>
        <input type="range" class="form-range border-0" id="nyn-settings-1" min="-3" max="3" step="0.03">
        <div class="d-flex justify-content-between">
            <div class="text-start">short</div>
            <div class="text-end">long</div>
        </div>
        <br /><br />
        <label for="nyn-settings-2" class="form-label">Intensity</label>
        <input type="range" class="form-range border-0" id="nyn-settings-2" min="-4" max="4" step="0.04">
        <div class="d-flex justify-content-between">
            <div class="text-start">low</div>
            <div class="text-end">high</div>
        </div>
        <br /><br />
        <label for="nyn-settings-3" class="form-label">Weight-bearing</label>
        <input type="range" class="form-range border-0" id="nyn-settings-3" min="-2" max="2" step="0.02">
        <div class="d-flex justify-content-between">
            <div class="text-start">light</div>
            <div class="text-end">heavy</div>
        </div>
        <br /><br />
        <label for="nyn-settings-4" class="form-label">Strength-increasing</label>
        <input type="range" class="form-range border-0" id="nyn-settings-4" min="-2" max="2" step="0.02">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-5" class="form-label">Team-based exercises</label>
        <input type="range" class="form-range border-0" id="nyn-settings-5" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">solo</div>
            <div class="text-end">team</div>
        </div>
        <br /><br />
        <label for="nyn-settings-6" class="form-label">Neuroplasticity</label>
        <input type="range" class="form-range border-0" id="nyn-settings-6" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">single-handed</div>
            <div class="text-end">ambidextrous</div>
        </div>
        <br /><br />
        <label for="nyn-settings-7" class="form-label">Required thought</label>
        <input type="range" class="form-range border-0" id="nyn-settings-7" min="-2" max="2" step="0.02">
        <div class="d-flex justify-content-between">
            <div class="text-start">mindless</div>
            <div class="text-end">intensive</div>
        </div>
        <br /><br />
        <label for="nyn-settings-8" class="form-label">Weight loss focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-8" min="-2" max="2" step="0.02">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-9" class="form-label">Upper body focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-9" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-10" class="form-label">Lower body focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-10" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-11" class="form-label">Full body focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-11" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-12" class="form-label">Core focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-12" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-13" class="form-label">Cardio focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-13" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-14" class="form-label">Flexibility focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-14" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
        <br /><br />
        <label for="nyn-settings-15" class="form-label">Balance focus</label>
        <input type="range" class="form-range border-0" id="nyn-settings-15" min="-1" max="1" step="0.01">
        <div class="d-flex justify-content-between">
            <div class="text-start">minimal focus</div>
            <div class="text-end">active pursuit</div>
        </div>
    </div>
    <br />
    <Button on:click={handleSettingsSubmission}>Save preferences</Button>
    <br /><br />
    <Button color=danger on:click={logOut}>Log out</Button>
</main>

<style>
    #nyn-settings-title {
        font-family: "Open Sans", sans-serif;
        font-weight: 700;
    }
    #nyn-form-box {
        width: 95%;
        max-width: 600px;
    }
    @media (max-width: 450px) {
        .nyn-fs-xem {
            font-size: 1.75rem !important;
        }
        .nyn-exp-text {
            font-size: 0.8rem !important;
        }
    }
    .nyn-fs-xem {
        font-size: 2rem;
    }
</style>