import { PUBLIC_BACKEND_URL } from "$env/static/public";

export async function logout () {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/api/auth/logout`, { method: "POST"})
        if (res.ok){
            return true
        }
    return false
}