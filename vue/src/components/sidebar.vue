<template>
  
  <div class="sidebar">
    <!-- 提示标签为网页logo，鼠标移动到logo上时会显示侧边栏，鼠标离开侧边栏时会隐藏侧边栏 -->
    <img id="logo" src="../assets/logo.png" @mouseover="showSidebar">
    <!-- 侧边栏 -->
    <div class="tip" v-show="isShowTip"></div>
    <div class="sidebar-box" v-show="isSidebarShown" @mouseleave="hideSidebar">
      <ul>
        <li>
          <!-- 未登录时显示登录、咨询、天气标签，登陆时显示用户姓名、网页、todo、咨询、天气、人流量、壁纸、退出标签 -->
          <a href="http://localhost:8000/login/" v-if="!islogin"> 登录 </a>
          <a v-else>{{ name }}</a>
        </li>
        <li><a href="#" @click.prevent="ChangeComponent('websites')">网页</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('todo')" v-if="islogin">todo</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('news')">资讯</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('weather')">天气</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('charts')" v-if="islogin">人流量</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('aibackground')" v-if="islogin">壁纸</a></li>
        <li><a href="http://localhost:8000/logout/" v-if="islogin">退出</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue';
  import axios from "axios";

  export default {
    name: 'Sidebar',
    setup(props, context) {
      const isSidebarShown = ref(false)
      const isShowTip = ref(true)
      const islogin = ref(false)
      const name = ref(null)

      //jaccount登录
      function showSidebar() {
        isSidebarShown.value = true
        isShowTip.value = false
        if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) islogin.value = false
        else {
          islogin.value = true
          name.value = sessionStorage.getItem("name")
        }
      }

      //隐藏侧边栏
      function hideSidebar() {
        isSidebarShown.value = false
      }

      //实现页面跳转
      const ChangeComponent = (component) => {
        context.emit("ChangeComponent", component);
      }

      return {
        isSidebarShown,
        isShowTip,
        islogin,
        name,
        showSidebar,
        hideSidebar,
        ChangeComponent
      }
    },
  }
</script>

<style scoped>
  .sidebar {
    position: fixed;
    top: 5%;
    left: 2%;
    width: 60px;
    height: 600px;
  }
  
  .tip{
    position: absolute;
    text-align: center;
    top:12%;
    width:100%;
    height: 3px;
    background-color: rgb(0, 6, 4);
  }
  #logo {
    position: absolute;
    text-align: center;
    left: 0px;
    width: 100%;
  }

  .sidebar-box {
    position: absolute;
    top: 15%;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.253);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    transition: right 0.3s ease-in-out;
  }

  .sidebar-box ul {
    list-style: none;
    display: flex;
    margin: 0;
    padding: 0;
    flex-direction: column;
    justify-content: space-around;
  }

  .sidebar-box li a {
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    height: 70px;
    font-size: large;
    text-decoration: none;
  }

  .sidebar-box li a:hover {
    background-color: rgba(255, 255, 255, 0.517);
  }
</style>