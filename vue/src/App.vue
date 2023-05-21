<template>
  <div id="app">
    <div id="head">
      <searchbox id="searchbox"></searchbox>
      <flip-clock></flip-clock>
      <charts id="charts" v-if="showcomponent === 'charts'"></charts>
    </div>
    <websites id="websites" v-if="showcomponent === 'websites'"></websites>
    <sidebar @ChangeComponent="ChangeComponent" ></sidebar>
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import Searchbox from './components/searchbox.vue'
import Sidebar from './components/sidebar.vue'
import websites from './components/websites.vue'
import charts from './components/charts.vue'
import {getview} from './api/api.js'
import {ref,onMounted} from 'vue'

export default {
  components: { FlipClock, websites, Searchbox, Sidebar, charts},
  name: 'App',
  setup()
  {
    const sites = ref([]);
    const showcomponent = ref();

    const getView = async() => {
      const response = await getView();
      sites.value = response.data["sites"];
      sessionStorage.setItem("name", response.data['name']);
      sessionStorage.setItem("jaccount", response.data['account']);
    };

    const ChangeComponent = (component) =>{
      showcomponent.value = component;
      console.log(component)
    }

    const printData = () => {
      //console.log(this.show)
    };

    onMounted(() => {
      getView();
      printData();
    } 
    );

    return{
      sites,
      getView,
      printData,
      showcomponent,
      ChangeComponent
    };
  },
  /*
  data () {
    return {
      sites: [], // 初始化空数组
      show:'websites'
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getView()
  },
  methods: {
    changeComponent(currentname){
      this.show = currentname
    },

    getView () {
      console.log(this.show)
      getview().then(response => {
        this.sites = response.data["sites"]
        // document.getElementById('response').innerHTML = response.data['sites']
        // 将name和jaccount存入session
        sessionStorage.setItem("name", response.data['name'])
        sessionStorage.setItem("jaccount", response.data['account'])
        console.log(this.show)
      })
    },
  }
  */
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

</style>
