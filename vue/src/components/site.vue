<template>
  <div> 
  <div class="sitesmallbox" ref="box" v-if="showsite">
    <a :href="siteUrl" target="_blank" @contextmenu.prevent="showbox" ref="delSite">
      <div class="img">
        <img :src="siteSrc">
      </div>
    </a>
    <p >{{ siteName }}</p>
    <div class="del_site" v-if="islogin&&delSite">
      <div class="delbox" @click="addBox"><a>修改</a></div>
      <div class="delbox" @click="delete_site"><a>删除</a></div>
    </div>
  </div>
  <div class="addSiteBox" v-if="siteFlag">
      <h1>修改网站名称</h1>
      <div class="box_form">
        <div class="item">
          <input
            type="text"
            placeholder="网站名称"
            id="site_name"
            name="site_name"
            required="required"
            v-model="addName"
          />
        </div>
        <a class="button1" @click="refactor_site">
          <input type="submit" value="完 成" id="site_submit" />
        </a>
        <div class="button2" @click="closeSite">
          <img src="../assets/close.png" />
        </div>
      </div>
    </div>
    <div class="massagebox" v-if="massageFlag">
      {{ noPermission }}
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "site",
  props: {
    siteUrl: String,
    siteSrc: String,
    siteName: String,
  },
  data() {
    return {
      showsite: true,
      delSite: false,
      siteFlag: false,
      massageFlag: false,
      islogin: false,
      noPermission: '',
    }
  },
  created() {
    this.getloginflag()
  },
  methods: {
    // 判断是否登录
    getloginflag (){
      setTimeout(() => {
          if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) this.islogin = false
          else {
            this.islogin = true
          }
        }, 500)
    },
    //出现修改删除框
    showbox(event) {
      this.delSite = true
      this.$nextTick(() => {
        this.$refs.delSite.style.top =
          this.$refs.box.offsetHeight - this.$refs.delSite.offsetHeight + "px";
        this.$refs.delSite.style.right = 0;
        document.addEventListener("click", this.hidebox);
      });
    },
    //点击任何地方隐藏修改删除框
    hidebox(event) {
      if (!this.$refs.box.contains(event.target)) {
        this.delSite = false;
        document.removeEventListener("click", this.hidebox);
      }
    },
    // 修改窗口出现
    addBox() {
      this.siteFlag = true;
      this.delSite = false;
    },
    // 弹窗
    showMessage(text) {
      this.noPermission = text;
      this.massageFlag = true;
      setTimeout(() => {
        this.massageFlag = false;
      }, 2000);
    },
    // 关闭修改窗口
    closeSite() {
      this.siteFlag = false;
      this.addName = "";
      this.addUrl = "";
    },
    // 修改site信息
    refactor_site() {
      const siteName = this.addName;
      this.siteFlag = false;
      var that = this;
      var params = new URLSearchParams();
      var jaccount = sessionStorage.getItem("jaccount");

      params.append("jaccount", jaccount); // jaccount也需要传递到后端
      params.append("refactor_site_name", siteName || ""); // 此处需要改成传入的siteName
      params.append("refactor_site_url", that.siteUrl); // 我们的功能是根据siteUrl来索引并修改siteName，因此that.siteUrl不用改

      // 发送POST请求
      axios
        .post("http://localhost:8000/index/refactor_site/", params)
        .then(function (response) {
          console.log(response.data["key"]);
          if (response.data["key"] == 1) {
            that.showMessage("网站修改成功！");
            location.reload();
          }
          if (response.data["key"] == 0) {
            that.showMessage("没有检测到您的输入！");
          }
        })
        .catch(function (error) {
          // 报错处理
          console.log(error);
        });
    },

    delete_site() {
      this.showbox = false;
      var that = this;
      var params = new URLSearchParams();
      var jaccount = sessionStorage.getItem("jaccount");
      params.append("jaccount", jaccount); // jaccount也需要传递到后端
      params.append("delete_site_name", that.siteName);
      // 发送POST请求
      axios
        .post("http://localhost:8000/index/delete_site/", params)
        .then(function (response) {
          console.log(response.data["key"]);
          if (response.data["key"] == 1) {
            that.showsite = false;
          }
        })
        .catch(function (error) {
          // 报错处理
          console.log(error);
        });
      this.addName = "";
    },
  },
};
</script>

<style>
.sitesmallbox {
  display: flex;
  position: relative;
  flex-direction: column;
  align-items: center;
  align-content: center;
  width: 120px;
  height: 100px;
  margin: 10px 0px;
}

.sitesmallbox .img {
  width: 70px;
  height: 70px;
  background-color: rgb(255, 255, 255, 0.5);
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2),
    -4px -4px 8px rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: box-shadow 0.2s ease-out;
  position: relative;
  backdrop-filter: blur(10px);
}

.sitesmallbox .img img {
  width: 45px;
  border-radius: 10px;
  transition: width 0.2s ease-out;
}

.sitesmallbox p {
  text-decoration: none;
  margin-top: 10px;
  color: dimgrey;
  text-shadow: 1px 1px lightgrey;
  font-size: 13px;
  align-content: center;
}

.sitesmallbox .img:hover {
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.2),
    0px 0px 0px rgba(255, 255, 255, 0.1), inset 4px 4px 4px rgba(0, 0, 0, 0.1),
    inset -4px -4px 4px rgba(255, 255, 255, 1);
  transition: box-shadow 0.2s ease-out;
}

.sitesmallbox .img:hover img {
  width: 40px;
  transition: width 0.2s ease-out;
}

.del_site {
  position: absolute;
  top: 30%;
  right: 0%;
  z-index: 999;
  color: black;
  border-radius: 10px;
}

.delbox {
  padding: 5px 10px;
  background-color: rgba(255, 255, 255, 0.94);
  border: 1px solid rgb(169, 169, 169);
  border-radius: 8px;
  font-size: 15px;
}
.delbox:hover {
cursor: pointer;
}

.addSiteBox {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
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
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2),
    -4px -4px 8px rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  transition: box-shadow 0.2s ease-out;
  position: relative;
}

.addSiteBox .box_form .button1 input:hover {
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.2),
    0px 0px 0px rgba(255, 255, 255, 0.1), inset 4px 4px 4px rgba(0, 0, 0, 0.1),
    inset -4px -4px 4px rgba(255, 255, 255, 1);
  transition: box-shadow 0.2s ease-out;
  cursor: pointer;
}

.addSiteBox .box_form .button2 {
  position: absolute;
  top: 5%;
  right: 5%;
}

.addSiteBox .box_form .button2:hover {
cursor: pointer;
}

.addSiteBox .box_form .button2 img {
  width: 30px;
}

.addSiteBox .box_form .date_list {
  margin-top: 20px;
  opacity: 1;
}

.addSiteBox .box_form .date_list select {
  background: #000000;
  opacity: 1;
}

.massagebox {
  background: rgba(255, 255, 255, 0.94);
  border-radius: 20px;
  color: #000000;
  position: absolute;
  z-index: 1000;
  padding: 10px 100px;
  left: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  text-align: center;
  font-size: 20px;
}
</style>
