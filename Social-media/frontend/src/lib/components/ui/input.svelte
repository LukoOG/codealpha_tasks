<script lang="ts">
	interface inputProps{
		type: string,
		className: string,
		value: string | number | undefined,
		disabled: boolean,
		placeholder: string,
		name: string,
		id: string,
	}
  
  let {
	type = "text",
	class: className = "",
	value,
	disabled = false,
	placeholder,
	name,
	id,
  }:inputProps = $props()
  
  
</script>

<input {name} {placeholder} {type} class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background 
         file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground 
         placeholder:text-muted-foreground 
         focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 
         disabled:cursor-not-allowed disabled:opacity-50 md:text-sm {className}" />
