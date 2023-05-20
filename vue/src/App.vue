<template>
  <div id="app">
    <div id="head">
      <img id="logo" src="./assets/logo.png">
      <searchbox id="searchbox"></searchbox>
      <flip-clock></flip-clock>
    </div>

    <websites id="websites" :sites="sites"></websites>
    <sidebar></sidebar>
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import Searchbox from './components/searchbox.vue'
import Sidebar from './components/sidebar.vue'
import websites from './components/websites.vue'
import {getview} from './api/api.js'
export default {
  components: { FlipClock, websites, Searchbox, Sidebar },
  name: 'App',
  data () {
    return {
      sites: [] // 初始化空数组
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getView()
  },
  methods: {
    getView () {
      getview().then(response => {
        this.sites = response.data["sites"]
        // document.getElementById('response').innerHTML = response.data['sites']

        // 将name和jaccount存入session
        sessionStorage.setItem("name", response.data['name'])
        sessionStorage.setItem("jaccount", response.data['account'])
        console.log(this.sites)
      })
    },
  }
}
</script>
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

</style>
