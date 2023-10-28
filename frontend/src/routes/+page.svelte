<script>
  import { onMount } from "svelte";
  import { Store } from "../store";
  onMount(async function(){
    if(!$Store.length){
        const endpoint="http://localhost:8000/"
        const response= await fetch(endpoint)
        const data = await response.json()
        console.log(data)
        Store.set(data)
    }
    
  })
    
</script>

<h1>Homepage</h1>

<h2>Data from test model</h2>
<ul>
    {#each $Store as item}
        <li>{item.name}</li>
    {/each}
</ul>