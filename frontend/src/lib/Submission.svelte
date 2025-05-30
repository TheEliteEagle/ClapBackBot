<script>
    // get comeback from flask server

    let user_input = '';
    export let comeback = '';

    async function handleSubmit(event) {

        event.preventDefault();

        try{
            comeback = 'Thinking...';
            const response = await fetch(
                'http://localhost:5000/comeback',
                {
                    method:'POST',
                    headers: {"Content-Type": "application/json"}, 
                    body: JSON.stringify({'roast': user_input})

            })

            const data = await response.json();
            comeback = data.comeback;
            console.log(comeback)
        } 
        
        catch (err) { 
            comeback = "Backend Error";
            console.error(err);
        }

    }
</script>

<form on:submit={handleSubmit}>
  <input bind:value={user_input} placeholder="Enter the roast" />
  <button type="submit">Send</button>
</form>

