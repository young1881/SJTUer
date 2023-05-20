<template>
  <div class="websites">
    <div class = "sitebox">
        <site v-for="item in sites" :key="item.site_name" :siteUrl="item.site_url" :siteSrc="item.site_src" :siteName="item.site_name"></site>
    </div>
  </div>
</template>

<script>
import site from './site.vue'
import {getview} from '../api/api.js'
export default {
  components: { site },
  name: 'websites',
  data () {
    return {
      sites: [] // 初始化空数组
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getSite()
  },
  methods: {
    getSite () {
      getview().then(response => {
        this.sites = response.data['sites']
        // document.getElementById('response').innerHTML = response.data['sites']

        // 将name和jaccount存入session
        sessionStorage.setItem("name", response.data['name'])
        sessionStorage.setItem("jaccount", response.data['account'])
        console.log(response.data['sites'][0]['site_url'])
      })
    },
  }
}
</script>

<style scoped>
.websites{
  display: flex;
  justify-content: center;
  align-items: center;

}
.sitebox{
  margin: 10%;
  padding: 10px;
  width: 40%;
  height: 300px;
  background-color: rgb(255,255,255,0.5);
  border-radius: 30px;
  display: flex;
  flex-wrap: wrap;
  align-content: start;
  align-items: flex-start;

}

/* 如果需要添加间距，在这里设置margin或padding即可 */
.sitebox site {
  margin-right: 0px;
  margin-bottom: 0px;
}
</style>
