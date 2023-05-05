import { BASE_URL } from "./constants"

export async function request (url, params = {}) {
    params = Object.assign({
        mode: 'cors',
        cache: 'no-cache',
    }, params)

    params.headers = Object.assign({
        'Content-Type': 'application/json'
    }, params.headers)

    let response = await fetch(BASE_URL + url, params)
    let json = await response.json() || {}
    if (!response.ok){
        let errorMessage = json.error || response.status
        throw new Error(errorMessage)
    }
    return json
}