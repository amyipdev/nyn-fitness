export async function loginFetch(usn: string, pwd: string, long: boolean): Promise<[number, string]> {
    const r = await fetch("/api/generate_token", {
        method: "POST",
        body: JSON.stringify({
            usn: usn,
            pwd: pwd,
            long: long
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });
    return [r.status, r.status == 200 ? (await r.json())["token"] : ""]
}