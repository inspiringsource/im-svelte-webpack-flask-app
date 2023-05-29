<script>
  import { onMount } from 'svelte';
  let products = [];
  let name = '';
  let description = '';
  let quantity = 0;

  // Function to fetch products
  async function fetchProducts() {
    const response = await fetch('http://localhost:5001/products');
    products = await response.json();
  }

  // Call fetchProducts on mount
  onMount(fetchProducts);

  async function deleteProduct(id) {
    await fetch(`http://localhost:5001/products/${id}`, { method: 'DELETE' });
    // Refresh products after deletion
    fetchProducts();
  }

  async function createProduct() {
    await fetch('http://localhost:5001/products', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: name,
        description: description,
        quantity: quantity
      })
    });
    // Refresh products after creation
    fetchProducts();
  }
</script>

<h1>Products</h1>

<form on:submit|preventDefault={createProduct}>
  <input bind:value={name} placeholder="Product name" />
  <input bind:value={description} placeholder="Product description" />
  <input type="number" bind:value={quantity} placeholder="Product quantity" />
  <button type="submit">Create Product</button>
</form>

<ul>
  {#each products as product (product.id)}
    <div>
      <h2>{product.name} 📦</h2>
      <p>Description: {product.description}</p>
      <p>SKU / ID: {product.id}</p>
      <p>Quantity: {product.quantity}</p>
      <button on:click={() => deleteProduct(product.id)}>Delete</button>
    </div>
  {/each}
</ul>
