<template>
  <div id="app">
    <div id="head">
      <img id="logo" src="./assets/logo.png">
      <searchbox id="searchbox"></searchbox>
      <flip-clock></flip-clock>
    </div>

    <websites id="websites"></websites>
    <sidebar></sidebar>
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import Searchbox from './components/searchbox.vue'
import Sidebar from './components/sidebar.vue'
import websites from './components/websites.vue'
export default {
  components: { FlipClock, websites, Searchbox, Sidebar },
  name: 'App'
}
</script>

<style>
body{
  background: rgb(254, 232, 253);
  z-index: -3;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
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
#searchbox {
    position: absolute;
    top: 230px;
    left: 50%;
    transform: translate(-50%, -50%);
    height: 50px;
    z-index:700;
}

</style>
