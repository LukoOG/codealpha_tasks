<script lang="ts">
	import { tv } from 'tailwind-variants';
	import type { Snippet } from 'svelte';

	type variantType = "default" | "outline" | "secondary" | "ghost" | "link";
	type sizeType = "default" | "sm" | "lg" | "icon";
	type buttonType = "button" | "submit" | "reset";
	
	interface buttonProps {
		variant: variantType,
		size: sizeType,
		class: string,
		type: buttonType,
		disabled: boolean,
		children: Snippet,
	}
	
	let { 
		variant = "default",
		size = "default",
		type = "button",
		class: className="",
		disabled = false,
		children, ...others
	}: buttonProps = $props()

  const button = tv({
    base: "inline-flex cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
		social: "bg-social-blue text-white hover:bg-social-blue-hover transition-all duration-200",
		like: "text-muted-foreground hover:text-social-red hover:bg-social-red/10 transition-all duration-200",
        "like-active": "text-social-red bg-social-red/10",
        repost: "text-muted-foreground hover:text-social-green hover:bg-social-green/10 transition-all duration-200",
        "repost-active": "text-social-green bg-social-green/10",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  });
</script>

<button {type} {...others} {disabled} class={ button({ variant, size, className }) }>
	<div class="contents">{@render children?.()}</div>
</button>