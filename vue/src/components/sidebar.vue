<template>
  <div class="sidebar">
    <!-- 提示标签 -->
    <div class="hint" v-show="!isSidebarShown" @mouseover="showSidebar">侧边栏</div>
    <!-- 侧边栏 -->
    <div class="sidebar-box" v-show="isSidebarShown" @mouseleave="hideSidebar">
      <ul>
        <li><a href="#">登录</a></li>
        <li><a href="#">todo</a></li>
        <li><a href="#">资讯</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sidebar',
  data () {
    return {
      isSidebarShown: false
    }
  },
  methods: {
    // 鼠标移入显示侧边栏
    showSidebar () {
      this.isSidebarShown = true
    },
    // 鼠标移出隐藏侧边栏
    hideSidebar () {
      this.isSidebarShown = false
    }
  }
}
</script>

<style scoped>
.sidebar {
  position: fixed;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 100px;
}

.hint {
  position: absolute;
  right: 0px;
  width: 60px;
  height: 60px;
  background-color: #777777;
  border-radius: 50%;
  color: #ffffff;
  text-align: center;
  line-height: 60px;
  font-size: 14px;
  cursor: pointer;
  transition: right 0.3s ease-in-out;
}

.sidebar-box {
  position: absolute;
  top: calc(50% - 110px);
  right: 0px; /* 隐藏侧边栏 */
  width: 50px;
  height: 200px;
  background-color: #ffffff;
  border-radius: 20px 0px 0px 20px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  transition: right 0.3s ease-in-out;
}

.sidebar-box ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 100%;
}

.sidebar-box li a {
  display: block;
  width: 100%;
  height: 100%;
  text-align: center;
  line-height: 60px;
  color: #333;
  text-decoration: none;
}

.sidebar-box li a:hover {
  background-color: #f5f5f5;
}
</style>
