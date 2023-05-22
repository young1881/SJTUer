<template>
    <div class="poem">
        <p class="sentence">{{`「 ${content} 」 ——《${origin}》 ${author}`}}</p>
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
