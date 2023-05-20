<template>
  <div class="websites">
    <div class = "sitebox">
        <site v-for="item in sites" :key="item.site_name" :siteUrl="item.site_url" :siteSrc="item.site_src" :siteName="item.site_name"></site>
    </div>
  </div>
</template>

<script>
import site from './site.vue'
export default {
  components: { site },
  name: 'websites',
  props: {
    sites: {
      type: Array,
      required: true
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getSite()
  },
  methods: {
    getSite () {
      console.log(this.site)
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
  width: 70%;
  background-color: rgb(255,255,255,0);
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
