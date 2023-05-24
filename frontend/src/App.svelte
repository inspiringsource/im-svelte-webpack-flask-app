<script>
	import { onMount } from 'svelte';
	import ProductList from './ProductList.svelte';
	import CreateProduct from './CreateProduct.svelte';
	import OrderList from './OrderList.svelte';
	import CreateOrder from './CreateOrder.svelte';

	let products = [];  // This line was missing

	onMount(async () => {
		const response = await fetch('http://localhost:5001/products');
		products = await response.json();
	});
</script>
  
<main>
	<h1>Inventory Management</h1>
  
	<ProductList />
	<!-- <CreateProduct /> -->
	<!-- <OrderList /> -->
	<CreateOrder />
</main>
