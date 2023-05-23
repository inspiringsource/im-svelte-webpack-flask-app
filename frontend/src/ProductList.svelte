<script>
    import { onMount } from 'svelte';
    let products = [];
  
    onMount(async () => {
      const response = await fetch('http://localhost:5001/products');
      products = await response.json();
    });
  </script>
  
  <h1>Products</h1>
  
  <ul>
    {#each products as product (product.id)}
      <li>
        <h2>{product.name}</h2>
        <p>{product.description}</p>
        <p>Quantity: {product.quantity}</p>
      </li>
    {/each}
  </ul>
  