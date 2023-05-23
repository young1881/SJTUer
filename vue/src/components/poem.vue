<template>
    <div class="poem">
        <p class="sentence">{{`「 ${poem.content} 」 ——《${poem.origin}》 ${poem.author}`}}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'poem',
    props: {
      poem: {
        type: Object,
        required: true
      }
    },
  }
  </script>


<style scoped>
.poem {
    position: absolute;
    top: 96%;
    left: 50%;
    width:700px;
    transform : translate(-50%,-50%);
    font-size: 15px;
    color: dimgrey;
    text-shadow: 1px 1px lightgrey;
    text-align:center;
}
</style>
