import { fail, redirect } from '@sveltejs/kit'
import type { Actions } from '@sveltejs/kit'
import { BACKEND_URL } from "$env/static/private"

export const load = ({ locals }) => {
    if (locals.user){
        redirect(302, '/')
    }
}

export const actions: Actions = {
    login: async ({ request, fetch }) => {
        const data = await request.formData();
        const email = data.get("email")
        const password = data.get("password")
        // console.log("logging in", email, password)
        // return

        const res = await fetch(
            `${BACKEND_URL}/api/auth/login`,
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({email, password}),
                credentials: "include"
            }
        )

        if(!res.ok){
            const error = await res.json().catch(() => ({}));
            return fail(res.status, { error });
        }

        throw redirect(303, '/')
    },

    register: async ({ request, fetch }) => {
        const data = await request.formData();
        const email = data.get("email")
        const password = data.get("password")
        console.log("registering", email, password)
        return
    }
}