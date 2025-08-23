let accessToken: string | null = null;
let refreshToken: string | null = null;

export function loadTokens() {
  accessToken = localStorage.getItem("accessToken");
  refreshToken = localStorage.getItem("refreshToken");
}

export function setTokens(tokens: { access: string; refresh: string }) {
  accessToken = tokens.access;
  refreshToken = tokens.refresh;
  localStorage.setItem("accessToken", tokens.access);
  localStorage.setItem("refreshToken", tokens.refresh);
}

async function refreshAccessToken() {
  if (!refreshToken) throw new Error("No refresh token");

  const res = await fetch("/api/auth/token/refresh", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh: refreshToken })
  });
 if (!res.ok) throw new Error("Failed to refresh token");

  const data = await res.json();
  accessToken = data.access;
  localStorage.setItem("accessToken", data.access);
  return accessToken;
}