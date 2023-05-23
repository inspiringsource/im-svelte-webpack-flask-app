<script>
    let productId = '';
    let quantity = '';
  
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
    }
  </script>
  
  <h1>Create Order</h1>
  
  <form on:submit|preventDefault={createOrder}>
    <label>
      Product ID:
      <input bind:value={productId} type="number" min="1" />
    </label>
    <label>
      Quantity:
      <input bind:value={quantity} type="number" min="1" />
    </label>
    <button type="submit">Create</button>
  </form>
  