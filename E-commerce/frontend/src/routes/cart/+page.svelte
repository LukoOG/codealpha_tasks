<script lang="ts">
    let { data } = $props()
</script>

<section class="min-h-screen bg-gradient-to-br from-orange-50 to-orange-100 p-6">
  <h1 class="text-2xl font-bold text-orange-600 mb-6">Your Cart</h1>

  <div class="space-y-4">
    {#each data.cart as item}
      <div class="bg-white/80 backdrop-blur-md shadow rounded-xl p-4 flex justify-between items-center">
        <div>
          <h3 class="font-medium">{item.name}</h3>
          <p class="text-sm text-gray-500">${item.price} × {item.quantity}</p>
        </div>
        <div class="flex items-center gap-2">
          <button class="px-2 bg-orange-200 rounded">-</button>
          <span>{item.quantity}</span>
          <button class="px-2 bg-orange-200 rounded">+</button>
        </div>
      </div>
    {/each}
  </div>

  <div class="mt-8 bg-white/80 backdrop-blur-md shadow rounded-xl p-6">
    <div class="flex justify-between mb-2">
      <span>Subtotal</span><span>$24.50</span>
    </div>
    <div class="flex justify-between font-bold text-orange-600">
      <span>Total</span><span>$28.50</span>
    </div>
    <button class="w-full bg-orange-500 text-white py-3 rounded-xl mt-4 hover:bg-orange-600">
      Checkout
    </button>
  </div>
</section>
