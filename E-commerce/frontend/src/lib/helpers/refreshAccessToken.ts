import {PUBLIC_BACKEND_URL} from "$env/static/public"

export default async function refreshAccessToken(event: any) {
  const refresh = event.cookies.get("refreshToken");
  if (!refresh) return null;
  
  console.log(refresh)

  try {
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/auth/token/refresh`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization":`Bearer ${refresh}` },
      body: JSON.stringify({ refresh: refresh }),
	  credentials:"include",
    });
	
	console.log(res)
	
    if (!res.ok) throw new Error("Failed to refresh access token");
    const data = await res.json();

    if (data.access) {
      // reset accessToken cookie
      event.cookies.set("accessToken", data.access, {
        httpOnly: true,
        secure: true,
        sameSite: "lax",
        path: "/",
        maxAge: 60 * 15
      });
      return data.access;
    }
  } catch (err) {
    console.error("Refresh token failed:", err);

    // Clear both cookies
    event.cookies.delete("accessToken", { path: "/" });
    event.cookies.delete("refreshToken", { path: "/" });

    return null;
  }
}