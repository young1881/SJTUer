<template>
  <div class="sitesmallbox" ref="box">
    <a :href="siteUrl" target="_blank" @contextmenu.prevent="showbox" ref="delSite">
      <div class="img">
        <img :src="siteSrc">
      </div>
    </a>
    <p >{{ siteName }}</p>
    <div class="del_site" v-if="delSite">
      <div class="delbox" @click="onEdit">修改</div>
      <div class="delbox" @click="onDelete">删除</div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    name: 'site',
    props: {
      siteUrl: String,
      siteSrc: String,
      siteName: String
    },
    data () {
    return {
      delSite: false
    }
  },
    methods: {
      showbox(event) {
      this.delSite = true
      this.$nextTick(() => {
        this.$refs.delSite.style.top = 
        this.$refs.box.offsetHeight - this.$refs.delSite.offsetHeight + 'px'
        this.$refs.delSite.style.right = 0
        document.addEventListener('click', this.hidebox)
      })
    },
    hidebox(event) {
      if (!this.$refs.box.contains(event.target)) {
        this.delSite = false
        document.removeEventListener('click', this.hidebox)
      }
    },
      // 修改site信息
    refactor_site() {
      var that = this
      var params = new URLSearchParams()
      var jaccount = sessionStorage.getItem("jaccount");
      // 需要传递的参数写到下方的第二个参数位置（此处用that.siteName来作展示，实际上应该是需要修改成传入的siteName）
      params.append('jaccount', jaccount);  // jaccount也需要传递到后端
      params.append('refactor_site_name', that.siteName);  // 此处需要改成传入的siteName
      params.append('refactor_site_url', that.siteUrl);  // 我们的功能是根据siteUrl来索引并修改siteName，因此that.siteUrl不用改

      // 发送POST请求
      axios
        .post('http://localhost:8000/index/refactor_site/', params)
        .then(function (response) {
          console.log(response.data['key'])
          // 如果后端修改成功，则返回response.data['key'] = 1；否则返回0
          // 需要重新加载整个页面才能获取更新后的值

    })
    .catch(function(error){
      // 报错处理
      console.log(error)
    })
    }
  }
  }
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
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2), -4px -4px 8px rgba(255, 255, 255, 0.5);
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
      0px 0px 0px rgba(255, 255, 255, 0.1),
      inset 4px 4px 4px rgba(0, 0, 0, 0.1),
      inset -4px -4px 4px rgba(255, 255, 255, 1);
    transition: box-shadow 0.2s ease-out;
  }

  .sitesmallbox .img:hover img {
    width: 40px;
    transition: width 0.2s ease-out;
  }

  .del_site{
    position: absolute;
    top: 40%;
    right: 10%;
    z-index: 999;
    background-color: rgba(255, 255, 255, 0.94);
    color: black;
    border-radius: 10px;
  }

  .delbox{
    padding: 10px;
  }
  .delbox a{
    font-size: 14px;
  }
</style>
