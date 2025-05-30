<script>
  import Submission from './lib/Submission.svelte'
  import character_image from './assets/character.png'

let comeback= 'I\'m ClapBackBot and I will generate you a comeback to a roast';
</script>


<main>

  {comeback}

  <div>
    <img src="{character_image}" alt="The ClapBackBot character" style="width: 300px">
  </div>

  <div class="card">
    <Submission bind:comeback />
  </div>

</main>

