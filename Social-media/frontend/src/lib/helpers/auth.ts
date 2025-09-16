export async function logout () {
	const res = await fetch("http://127.0.0.1:8000/api/auth/logout", { method: "POST"})
        if (res.ok){
            return true
        }
    return false
}