<script lang="ts">
	let name = '';
	let greeting = 'Welcome stranger 🥷';
	const getGreeting = () => {
	  fetch("/greet", {method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name })})
		.then(d => d.text())
		.then(d => (greeting = d));
	}
  </script>
  
  <h1>{greeting}</h1>
  <input type="text" bind:value={name} placeholder="What is your name?">
  <button on:click={getGreeting}>Greet me</button>