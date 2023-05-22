<template>
  <div id="app">
    <div id="head">
      <searchbox id="searchbox"></searchbox>
      <flip-clock></flip-clock>
      <charts id="charts" v-if="showcomponent === 'charts'" @library = "library"></charts>
    </div>
    <websites id="websites" v-if="showcomponent === 'websites'" :sites = "sites"></websites>
    <sidebar @ChangeComponent="ChangeComponent" ></sidebar>
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import Searchbox from './components/searchbox.vue'
import Sidebar from './components/sidebar.vue'
import websites from './components/websites.vue'
import charts from './components/charts.vue'
import {getview,getscrapy} from './api/api.js'
import {ref,onMounted,watch} from 'vue'

export default {
  components: { FlipClock, websites, Searchbox, Sidebar, charts},
  name: 'App',
  setup()
  {
    const sites = ref([]);
    const showcomponent = ref('websites');
    const library = ref([])

    const getView = async() => {
      const response = await getview();
      sites.value = response.data["sites"];
      sessionStorage.setItem("name", response.data['name']);
      sessionStorage.setItem("jaccount", response.data['account']);
    };

    const getScrapy = async() => {
      const response = await getscrapy();
      console.log("response")
      library.value = response.data["library"]
      console.log(library.value)
      console.log(library.value[0].inCounter)
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

    watch(() => showcomponent.value, (newVal, oldVal) => {
      if (newVal === 'charts') {
        getScrapy();
      }
    });

    return{
      sites,
      library,
      getView,
      printData,
      showcomponent,
      ChangeComponent
    };
  },
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
