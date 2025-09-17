<script lang="ts">
	interface textareaProps{
		className: string,
		value: string | undefined,
		placeholder: string | undefined,
		name: string | undefined,
		id: string | undefined,
		disabled: boolean,
		rows: number | undefined,
	}
  // forward reference to the raw DOM element
  //let textareaEl: HTMLTextAreaElement;
  //export { textareaEl as ref };
  
  let {
	className = "",
	value,
	placeholder,
	name,
	id,
	disabled = false,
	rows,
	...others
  }: textareaProps = $props()
</script>

<textarea
  bind:value={value}
  {placeholder}
  {name}
  {id}
  {disabled}
  {rows}
  class="flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background 
         placeholder:text-muted-foreground 
         focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 
         disabled:cursor-not-allowed disabled:opacity-50 {className}"
  {...others}
></textarea>
