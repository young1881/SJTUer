<template>
  <div class="sidebar">
    <!-- 提示标签 -->
    <img id="logo" src="../assets/logo.png" @mouseover="showSidebar">
    <!-- 侧边栏 -->
    <div class="sidebar-box" v-show="isSidebarShown" @mouseleave="hideSidebar">
      <ul>
        <li>
          <a href="http://localhost:8000/login/" v-if="!islogin"> 登录 </a>
          <a v-else>{{ name }}</a>
        </li>
        <li><a href="#" @click.prevent="ChangeComponent('websites')">网页</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('todo')">todo</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('news')">资讯</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('weather')">天气</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('charts')">人流量</a></li>
        <li><a href="#" @click.prevent="ChangeComponent('aibackground')">壁纸</a></li>
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
      const islogin = ref(false)
      const name = ref(null)

      function showSidebar() {
        isSidebarShown.value = true
        if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) islogin.value = false
        else {
          islogin.value = true
          name.value = sessionStorage.getItem("name")
        }
      }

      function hideSidebar() {
        isSidebarShown.value = false
      }

      const ChangeComponent = (component) => {
        context.emit("ChangeComponent", component);
        console.log(component)
      }


      return {
        isSidebarShown,
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