<script>
	let rand = -1;
  
	function getRand() {
	  fetch("http://localhost:5001/rand")
		.then(response => response.text())
		.then(data => rand = data);
	}
  </script>
  
  <h1>Your number is {rand}!</h1>
  <button on:click={getRand}>Get a random number</button>