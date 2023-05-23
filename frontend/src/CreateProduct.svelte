<script>
    let name = '';
    let description = '';
    let quantity = '';
  
    async function createProduct() {
      const response = await fetch('http://localhost:5001/products', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, description, quantity: +quantity }),
      });
      const newProduct = await response.json();
      // Here you might want to add the new product to the list of products
      // For now, we'll just log it
      console.log(newProduct);
    }
  </script>
  
  <h1>Create Product</h1>
  
  <form on:submit|preventDefault={createProduct}>
    <label>
      Name:
      <input bind:value={name} />
    </label>
    <label>
      Description:
      <input bind:value={description} />
    </label>
    <label>
      Quantity:
      <input bind:value={quantity} type="number" min="0" />
    </label>
    <button type="submit">Create</button>
  </form>
  