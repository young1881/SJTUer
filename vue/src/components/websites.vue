<template>
  <div class="websites">
    <div class = "sitebox">
        <site v-for="item in sites" :key="item.site_name" :siteUrl="item.site_url" :siteSrc="item.site_src" :siteName="item.site_name"></site>
        <div class="sitesmallbox">
          <a @click="addSite">
          <div class="img">
            <img :src="'#'">
          </div>
          </a>
          <p>新增收藏网站</p>
        </div>
    </div>

    <div class="addSiteBox" v-if="siteFlag">
      <h1>添加网站收藏</h1>
        <form>
          <div class = "box_form">
            <div class = "item">
              <input type="text" placeholder="网站名称" id="site_name" name="site_name" required="required">
            </div>
            <div class = "item">
              <input type="text" placeholder="网址" id="site_url" name="site_url" required="required" >
            </div>
            <a class = "button1" @click="closeSite">
              <input type="submit" value="完 成" id="site_submit"/>
            </a>
            <div class = "button2" @click="closeSite">
              <a> 取 消</a>
            </div>
          </div>
        </form>
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
  data () {
    return {
      siteFlag: false,
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getSite()
  },
  methods: {
    getSite () {
      console.log(this.site)
    },
    closeSite () {
      this.siteFlag = false
    },
    addSite (){
      this.siteFlag = true
    }
  }
}
</script>

<style scoped>
.websites{
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;

}
.sitebox{
  margin-top: 8%;
  padding: 10px;
  width: 70%;
  border-radius: 30px;
  z-index: 200;
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

.addSiteBox{
  position: absolute;
  top: 36%;
  left: 35%;
  width: 30%;
  padding-top: 20px;
  padding-bottom: 20px;
  background: rgba(255, 255, 255, 0.94);
  z-index:2000;
  overflow: auto;
  text-align: center;
  border-radius: 20px;
}

.addSiteBox h1{
    font-size: 30px;
    letter-spacing: 2px;
    font-family: Microsoft Yahei;
    color: #161718;
}

.addSiteBox h4{
    color: #111111;
}

.addSiteBox .box_form{
    margin-top: 30px;
}

.addSiteBox .box_form .item{
    margin-top: 15px;
}

.addSiteBox .box_form .item input{
    width: 200px;
    font-size: 18px;
    border: 0;
    border-bottom: 4px solid #000;
    padding: 5px 10px;
    background: #ffffff00;
    color: #000;
}

.addSiteBox .box_form .item input::placeholder{
    color: #00000099;
}

.addSiteBox .box_form .button1 input{
    margin: 0px auto;
    margin-top: 35px;
    width: 120px;
    height: 40px;
    font-size: 20px;
    font-weight: 600;
    border: 0;
    background-color: rgb(255, 255, 255,0.5);
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2), -4px -4px 8px rgba(255, 255, 255, 0.5);
    border-radius: 20px;
    transition: box-shadow 0.2s ease-out;
    position: relative;

}
.addSiteBox .box_form .button1 input:hover {
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.2),
  0px 0px 0px rgba(255, 255, 255, 0.1),
  inset 4px 4px 4px rgba(0, 0, 0, 0.1),
  inset -4px -4px 4px rgba(255, 255, 255, 1);
  transition: box-shadow 0.2s ease-out;
}

.addSiteBox .box_form .button2{
  position: absolute;
  top:5%;
  right: 5%;
}

.addSiteBox .box_form .button2 a{
    color:#00000099;
}

.addSiteBox .box_form .date_list{
    margin-top: 20px;
    opacity: 1;
}

.addSiteBox .box_form .date_list select{
    background: #000000;
    opacity: 1;
}
</style>
