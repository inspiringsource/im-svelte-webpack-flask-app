<script>
  import { onMount } from 'svelte';
  let orders = [];
  let productId = '';
  let quantity = '';

  // Function to fetch orders
  async function fetchOrders() {
    const response = await fetch('http://localhost:5001/orders');
    orders = await response.json();
  }

  // Call fetchOrders on mount
  onMount(fetchOrders);

  async function deleteOrder(id) {
    await fetch(`http://localhost:5001/orders/${id}`, { method: 'DELETE' });
    // Refresh orders after deletion
    fetchOrders();
  }

  async function createOrder() {
    const response = await fetch('http://localhost:5001/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ productId: +productId, quantity: +quantity }),
    });
    const newOrder = await response.json();
    // Here you might want to update the quantity of the relevant product and add the new order to the list of orders
    // For now, we'll just log it
    console.log(newOrder);

    // Refresh orders after creation
    fetchOrders();
  }
</script>

<h1>Create Order</h1>

<form on:submit|preventDefault={createOrder}>
  <label>
    SKU / ID:
    <input bind:value={productId} type="number" min="1" />
  </label>  <!-- Stock Keeping Unit is the product ID -->
  <label>
    Quantity:
    <input bind:value={quantity} type="number" min="1" />
  </label>
  <button type="submit">Create</button>
</form>

<h2>Orders</h2>

<ul>
  {#each orders as order (order.id)}
    <li>
      <h2>Order ID: {order.id}</h2>
      <p>Product ID: {order.productId}</p>
      <button on:click={() => deleteOrder(order.id)}>Delete</button>
    </li>
  {/each}
</ul>
