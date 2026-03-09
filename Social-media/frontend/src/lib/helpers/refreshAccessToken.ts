import { PUBLIC_BACKEND_URL } from '$env/static/public';

export default async function refreshAccessToken(event: any): Promise<string|undefined> {
	const refresh = event.cookies.get('refreshToken');
	const access = event.cookies.get('accessToken')
	if (!refresh) return;

	try {
		const res = await fetch(`${PUBLIC_BACKEND_URL}/api/auth/token/refresh`, {
			method: 'POST',
			headers: {
				Authorization: access ? `Bearer ${access}` : "",
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ refresh }),
			credentials: 'include'
		});

		if (!res.ok) throw new Error('Failed to refresh access token');
		const data = await res.json();
		// console.log("refresh response", data)

		if (data.access && data.refresh) {
			// reset accessToken cookie
			event.cookies.set('accessToken', data.access, {
				httpOnly: true,
				secure: true,
				sameSite: 'lax',
				path: '/',
				maxAge: 60 * 15
			});

			event.cookies.set('refreshToken', data.refresh, {
				httpOnly: true,
				secure: true,
				sameSite: 'lax',
				path: '/',
				maxAge: 60 * 60 * 24
			})
			return data.access;
		}
	} catch (err) {
		console.error('Refresh token failed:', err);

		// Clear both cookies
		event.cookies.delete('accessToken', { path: '/' });
		event.cookies.delete('refreshToken', { path: '/' });

		return;
	}
}
