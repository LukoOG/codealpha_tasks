import type { RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies }) => {
	// remove cookies
	cookies.delete('accessToken', { path: '/' });
	cookies.delete('refreshToken', { path: '/' });

	return new Response(
		JSON.stringify({ success: true }),
		{ status: 200, headers: { 'Content-Type': 'application/json' } }
	);
};
