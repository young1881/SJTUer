<template>
    <div class="poem" id="poem">
        <p class="sentence" id="sentence">「 {{ content }} 」</p>
        <p class="sentence" id="author">——《{{ origin }}》 {{ author }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        content: "梨花自寒食，进节只愁余。",
        origin:"寒食上冢",
        author:"杨万里",
      };
    },
  };
  </script>

<style scoped>
.poem {
    position: absolute;
    top: 94%;
    left: 50%;
    transform : translate(-50%,-50%);
    height :30px;
    font-size: 10px;
    background-color: brown;
    color: dimgrey;
    text-shadow: 1px 1px lightgrey;
    text-align:center;
}

#sentence{
    background-color: blue;
}

</style>
