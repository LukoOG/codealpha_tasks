// See https://svelte.dev/docs/kit/types#app.d.ts

import type { JwtPayload } from "jsonwebtoken";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
		interface Locals {
			user: string | JwtPayload | null
		}
	}
}

export {};
