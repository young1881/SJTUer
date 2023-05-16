<template>
  <div id="app">
    <div id="head">
      <img id="logo" src="./assets/logo.png">
      <flip-clock></flip-clock>
    </div>

    <websites></websites>

  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import websites from './components/websites.vue'
export default {
  components: { FlipClock, websites },
  name: 'App'
}
</script>

<style>
body{
  background: rgb(254, 232, 253);
  z-index: -3;
}

#head{
  margin-top: 5%;

}
#logo{
  position:absolute;
  top: 30px;
  left: 30px;
  width: 5%;
}

</style>
