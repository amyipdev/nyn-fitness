<script lang="ts">
    import Cookies from 'js-cookie';
    import Gallery from "./GalleryComponents/Gallery.svelte";
    import type {GalleryWorkout} from "./GalleryComponents/GalleryWorkout.js";
    import {Container,Row,Col,Icon} from "sveltestrap";
    
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
    <div class="my-2">
        <Container>
            <Row>
                <div class="d-flex justify-content-between">
                    <Col xs="4">
                        <div class="d-flex align-items-center">
                            <img id="nyn-logo-img" src="favicon.png" alt="Logo">
                            <h1 id="nyn-logo-home-txt" class="text-light">&nbsp;&nbsp;&nbsp;NYN Fitness</h1>
                        </div>
                    </Col>
                    <div class="d-flex align-items-center justify-content-end">
                        <Col xs="2">
                            <i id="nyn-settings-button" class="bi bi-gear-fill pe-4"/>
                        </Col>
                    </div>
                </div>
            </Row>
        </Container>
    </div>
    <br />
    {#if loaded}
        {#each dat as gal, index}
            <!--<h2 style="text-align: left;">{names[index]}</h2>-->
            <Gallery wks={gal} galname={names[index]} />
            <br />
        {/each}
    {/if}
</main>

<style>
    @media (max-width: 425px) {
        #nyn-logo-home-txt {
            display: none;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 426px) and (max-width: 767px) {
        #nyn-logo-home-txt {
            font-size: 0.8rem !important;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 768px) and (max-width: 989px) {
        #nyn-logo-home-txt {
            font-size: 1.2rem !important;
        }
        #nyn-logo-img {
            height: 36px !important;
        }
    }
    @media (min-width: 990px) and (max-width: 1199px) {
        #nyn-logo-home-txt {
            font-size: 1.8rem !important;
        }
        #nyn-logo-img {
            height: 48px !important;
        }
    }
    #nyn-logo-img {
        height: 64px;
    }
    #nyn-logo-home-txt {
        font-size: 2.8rem;
        text-decoration: none;
        font-weight: 700;
        font-family: 'Open Sans', sans-serif;
    }
    #nyn-settings-button {
        font-size: 1.3rem;
        transition: font-size 0.4s;
    }
    #nyn-settings-button:hover {
        font-size: 1.8rem;
    }
</style>