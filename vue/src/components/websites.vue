<template>
  <div class="websites">
    <div class = "sitebox">
        <site v-for="item in sites" :key="item.site_name" :siteUrl="item.site_url" :siteSrc="item.site_src" :siteName="item.site_name"></site>
        <div class="sitesmallbox">
          <a @click="addBox">
          <div class="img">
            <img :src="'#'">
          </div>
        </a>
        <p>新增收藏网站</p>
      </div>
    </div>

    <div class="addSiteBox" v-if="siteFlag">
      <h1>添加网站收藏</h1>
        <div class = "box_form">
          <div class = "item">
            <input type="text" placeholder="网站名称" id="site_name" name="site_name" required="required" v-model="addName">
          </div>
          <div class = "item">
            <input type="text" placeholder="网址" id="site_url" name="site_url" required="required" v-model="addUrl">
          </div>
          <a class = "button1" @click="addSite">
            <input type="submit" value="完 成" id="site_submit"/>
          </a>
          <div class = "button2" @click="closeSite">
            <img src="../assets/close.png">
          </div>
        </div>
    </div>

    <div class="massagebox" v-if="massageFlag">
      {{noPermission}}
    </div>
  </div>
</template>

<script>
import site from './site.vue'
import axios from "axios";
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
      massageFlag: false,
      noPermission: '',
    }
  },
  created () { // 在创建实例时一次性获取数据
    this.getSite()
  },
  methods: {
    getSite () {
      console.log(this.site)
    },
    addBox () {
      this.siteFlag = true
    },
    showMessage (text) {
      this.noPermission = text
      this.massageFlag = true
      setTimeout(() => {
        this.massageFlag = false
      }, 2000)
    },
    closeSite () {
      this.siteFlag = false
      this.addName = ''
      this.addUrl = ''
    },
    addSite(){
      this.siteFlag = false
      const siteName = this.addName
      const siteUrl = this.addUrl

      var that = this
      var params = new URLSearchParams()
      var jaccount = sessionStorage.getItem("jaccount")
      // 需要传递的参数写到下方的第二个参数位置（此处用that.siteName来作展示，实际上应该是需要修改成传入的siteName）
      params.append('jaccount', jaccount),  // jaccount也需要传递到后端
      params.append('site_name', siteName || ''), // 需要改成传入的siteName
      params.append('site_url', siteUrl || ''),  // 需要改成传入的siteUrl

      // 发送POST请求
      axios
      .post('http://localhost:8000/index/add_site/',params)
      .then(function(response){
        console.log(response.data['key'])
        if((response.data['key']==1)||(response.data['key']==2)){
          if(response.data['key']==1){
            that.showMessage("网站添加成功！")
          }
          if(response.data['key']==2){
            that.showMessage("该网址已存在，已将其重命名！")
          }
          location.reload()
        }
        if((response.data['key']==0)){
          that.showMessage("超出添加上限，请删除不需要的网址后再添加！")
        }
        if((response.data['key']==3)){
          that.showMessage("没有检测到您的输入！")
        }
        // 如果后端修改成功，则返回response.data['key'] = 1
        // 否则以下需要弹窗警告
        // 返回0表示：超出添加上限，请删除不需要的网址后再添加！
        // 返回2表示：该网址已存在，已将其重命名！
        // 返回3表示：没有检测到您的输入！

        // 若返回1，需要重新加载整个页面才能获取更新后的值

      })
      .catch(function(error){
        // 报错处理
        console.log(error)
      })

      this.addName = ''
      this.addUrl = ''
    },
  }
}

</script>

<style scoped>
  .websites {
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
  }

  .sitebox {
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

  .sitebox site {
    margin-right: 0px;
    margin-bottom: 0px;
  }

  .addSiteBox {
    position: absolute;
    top: 36%;
    left: 35%;
    width: 30%;
    padding-top: 20px;
    padding-bottom: 20px;
    background: rgba(255, 255, 255, 0.94);
    z-index: 2000;
    overflow: auto;
    text-align: center;
    border-radius: 20px;
  }

  .addSiteBox h1 {
    font-size: 30px;
    letter-spacing: 2px;
    font-family: Microsoft Yahei;
    color: #161718;
  }

  .addSiteBox h4 {
    color: #111111;
  }

  .addSiteBox .box_form {
    margin-top: 30px;
  }

  .addSiteBox .box_form .item {
    margin-top: 15px;
  }

  .addSiteBox .box_form .item input {
    width: 200px;
    font-size: 18px;
    border: 0;
    border-bottom: 4px solid #000;
    padding: 5px 10px;
    background: #ffffff00;
    color: #000;
  }

  .addSiteBox .box_form .item input::placeholder {
    color: #00000099;
  }

  .addSiteBox .box_form .button1 input {
    margin: 0px auto;
    margin-top: 35px;
    width: 120px;
    height: 40px;
    font-size: 20px;
    font-weight: 600;
    border: 0;
    background-color: rgb(255, 255, 255, 0.5);
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

  .addSiteBox .box_form .button2 {
    position: absolute;
    top: 5%;
    right: 5%;
  }

.addSiteBox .box_form .button2 img{
  width: 30px;
}

.addSiteBox .box_form .date_list{
    margin-top: 20px;
    opacity: 1;
  }

  .addSiteBox .box_form .date_list select {
    background: #000000;
    opacity: 1;
}

.massagebox{
  background: rgba(255, 255, 255, 0.94);
  border-radius:20px;
  color: #000000;
  position: absolute;
  z-Index: 1000;
  padding: 10px 100px;
  left: 50%;
  transform : translate(-50%,-50%);
  top: 50%;
  text-align: center;
  font-size: 20px;

}
</style>
