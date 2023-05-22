<template>
  <div id="app">
    <div id="head">
      <searchbox id="searchbox"></searchbox>
      <flip-clock></flip-clock>
        <charts id="charts" v-if="showcomponent === 'charts' &&scrapyFlag" :library = "library" :canteen = "canteen"></charts>
    </div>
    <websites id="websites" v-if="showcomponent === 'websites'" :sites = "sites"></websites>
    <sidebar @ChangeComponent="ChangeComponent" ></sidebar>
    <poem></poem>
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
import poem from './components/poem.vue'


export default {
  components: { FlipClock, websites, Searchbox, Sidebar, charts, poem},
  name: 'App',
  setup()
  {
    const sites = ref([]);
    const showcomponent = ref('websites');
    const library = ref([])
    const canteen = ref([])
    const scrapyFlag = ref(false)

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
      canteen.value = response.data["canteen"]
      scrapyFlag.value = true
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
      canteen,
      getView,
      printData,
      showcomponent,
      ChangeComponent,
      scrapyFlag
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
