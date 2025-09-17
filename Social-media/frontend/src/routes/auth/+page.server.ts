import { fail, redirect } from '@sveltejs/kit';
import { splitCookiesString, parse } from 'set-cookie-parser';
import type { Actions } from '@sveltejs/kit';
import { PUBLIC_BACKEND_URL } from "$env/static/public";

export const load = ({ locals }) => {
    if (locals.user){
        redirect(302, '/')
    }
}

export const actions: Actions = {
    login: async ({ request, fetch, cookies }) => {
        const data = await request.formData();
        const email = data.get("email")
        const password = data.get("password")

        const res = await fetch(
            `${PUBLIC_BACKEND_URL}/api/auth/login`,
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({email, password}),
                credentials: "include"
            }
        )

        // I have to manually set the cookies
        const rawCookies = res.headers.get("set-cookie");
		if(rawCookies){
			const cookiesArray = parse(splitCookiesString(rawCookies));
			for (const c of cookiesArray){
				cookies.set(c.name, c.value, {
					httpOnly: c.httpOnly ?? true,
					secure: c.secure,
					sameSite: (c.sameSite?.toLowerCase() as 'lax' | 'strict' | 'none') ?? 'lax',
					path: c.path ?? "/",
					...(c.maxAge ? { maxAge : c.maxAge} : {}),
					...(c.expires ? { expires: new Date(c.expires) } : {}),
				})
			}
		}


        if(!res.ok){
            const error = await res.json().catch(() => ({}));
            return fail(res.status, { error });
        }

        throw redirect(303, '/')
    },

    register: async ({ request, fetch, cookies }) => {
        const data = await request.formData();
        const email = data.get("email")
        const password = data.get("password")
        
        const res = await fetch(
            `${PUBLIC_BACKEND_URL}/api/auth/register`,
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({email, password}),
                credentials: "include",
            }
        )

        if(!res.ok){
            const error = await res.json().catch(() => ({}));
            return fail(res.status, { error });
        }

        throw redirect(303, '/auth/?form_state=login')
    }
}