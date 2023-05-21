import { createApp } from 'vue'
import ECharts from 'vue-echarts';
import App from './App.vue';
import 'echarts';

/*
Object.defineProperty(Vue.prototype, 'flag', {
    value: true
  });
*/

createApp(App)
    .component('ECharts', ECharts)
    .mount('#app');



