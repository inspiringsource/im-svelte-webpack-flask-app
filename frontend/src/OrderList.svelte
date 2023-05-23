<script>
    import { onMount } from 'svelte';
    let orders = [];
  
    onMount(async () => {
      const response = await fetch('http://localhost:5001/orders');
      orders = await response.json();
    });
  </script>
  
  <h1>Orders</h1>
  
  <ul>
    {#each orders as order (order.id)}
      <li>
        <h2>Order #{order.id}</h2>
        <p>Product ID: {order.productId}</p>
        <p>Quantity: {order.quantity}</p>
      </li>
    {/each}
  </ul>
  