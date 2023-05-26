<template>
  <div class="wallpapers" id="wallpapers">
    <b class="wallpaper_btn" id="preset">预设炫彩壁纸</b>
    <div class="wallpaperBox">
      <div class="color_wallpaper">
        <div class="color_wallpaper_img" id="DustyGrass" @click="change_color_wallpaper($event)"></div>
        <div class="color_wallpaper_desc">Dusty Grass</div>
      </div>
      <div class="color_wallpaper">
        <div class="color_wallpaper_img" id="NightFade" @click="change_color_wallpaper"></div>
        <div class="color_wallpaper_desc">Night Fade</div>
      </div>
      <div class="color_wallpaper">
        <div class="color_wallpaper_img" id="WinterNeva" @click="change_color_wallpaper"></div>
        <div class="color_wallpaper_desc">Winter Neva</div>
      </div>
      <div class="color_wallpaper">
        <div class="color_wallpaper_img" id="SunnyDay" @click="change_color_wallpaper"></div>
        <div class="color_wallpaper_desc">Sunny Day</div>
      </div>
      <div class="color_wallpaper">
        <div class="color_wallpaper_img" id="RareWind" @click="change_color_wallpaper"></div>
        <div class="color_wallpaper_desc">Rare Wind</div>
      </div>
    </div>
    <b class="wallpaper_btn" id="upload">上传本地图片</b>
    <div class="wallpaper">
      <form id="upload_img_form">
        <div class="upload">
          <input type="file" name="upload_file" id="upload_file">
        </div>
        <div class="button3">
          <a href="javascript:void(0)" @click="upload_img">
            <input id="submit_wp" type="submit" value="提 交">
          </a>
        </div>
      </form>
    </div>
    <b class="wallpaper_btn" id="aidraw">AI创作壁纸</b>
    <div class="ai_wallpaper">
      <div class="prompt_form">
        <input class="prompt_txt" id="prompt_txt" placeholder="输入提示词或句子，支持中英文，例如：赛博朋克, 城市, 霓虹灯, 科幻, 未来, 高清, 无水印, 详细">
      </div>
      <div class="highres_form">
        <input type="checkbox" id="need_highres" name="need_highres" value = "need_highres">生成高清图像（耗时较长）
      </div>
      <input id="submit_aidraw" type="submit" v-show="!isLoading" @click="submit_aidraw" value="提 交">
      <div class="loading_aidraw" v-show="isLoading">
        <img src="..\assets\loading.gif" id="loading_gif">创作中，请稍候...
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from "axios";
import { createForLoopParams } from '@vue/compiler-core';
  export default {
    name: 'aibackground',
    methods: {
      change_color_wallpaper: function(e) {
        var name = e.target.id;
        var css = name_to_css(name);
        var that = this;
        document.querySelector('body').setAttribute('style', 'background:' + css)

        var params = new URLSearchParams();
        var jaccount = sessionStorage.getItem("jaccount");

        params.append("jaccount", jaccount); // jaccount也需要传递到后端
        params.append("css", css); 

        // 发送POST请求
        axios
          .post("http://localhost:8000/index/color_wallpaper/", params)
          .then(function (response) {
            console.log("Wallpaper:");
            console.log(response.data["key"]);
            if (response.data["key"] == 1) {
              console.log("壁纸修改成功！");
            }
            if (response.data["key"] == 0) {
              console.log("壁纸修改失败！");
            }
          })
          .catch(function (error) {
            // 报错处理
            console.log(error);
          });
      },
      upload_img: function() {
        var file = document.getElementById('upload_file').files[0];
        var formData = new FormData()

        console.log("upload_wallpaper_file:")
        console.log(file);
        
        var params = new URLSearchParams();
        var jaccount = sessionStorage.getItem("jaccount");

        // params.append("jaccount", jaccount); // jaccount也需要传递到后端
        // params.append("upload_file", file); 

        formData.append("jaccount", jaccount);
        formData.append("upload_file", file)

        // 发送POST请求
        axios
          .post("http://localhost:8000/index/upload_img/", formData)
          .then(function (response) {
            console.log("Wallpaper:");
            console.log(response.data["key"]);
            if (response.data["key"] == 1) {
              console.log("壁纸文件修改成功！");
            }
            if (response.data["key"] == 0) {
              console.log("壁纸文件修改失败！");
            }
          })
          .catch(function (error) {
            // 报错处理
            console.log(error);
          });
      },
    },
    setup(props, context) {
      const isLoading = ref(false)
      function submit_aidraw() {
        isLoading.value = true
        var params = new URLSearchParams();
        var jaccount = sessionStorage.getItem("jaccount");

        params.append("jaccount", jaccount); // jaccount也需要传递到后端

        // 下方分别传三个参数：prompt, 页面大小的列表（必须是整型），是否勾选
        params.append("prompt", context); 
        params.append("page_size", context); 
        params.append("need_highres", context); 

        // 发送POST请求
        axios
          .post("http://localhost:8000/index/aidraw/", params)
          .then(function (response) {
            console.log("Wallpaper:");
            console.log(response.data["key"]);
            if (response.data["key"] == -1) {
              console.log("壁纸生成失败！");
            }
            else
            {
              // res['key'] 这里返回了一个地址，前端添加壁纸只需要写src=127.0.0.1:8000/ + 这个地址即可
              // res['key']形式为：media/bg_202305241829_origin.png
            }
          })
          .catch(function (error) {
            // 报错处理
            console.log(error);
          });
      }
      return {
        isLoading,
        submit_aidraw
      }
    }
  }

  function name_to_css(name) {
  if (name === "NightFade") {
    return "linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
  } else if (name === "WinterNeva") {
    return "linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%)"
  } else if (name === "SunnyDay") {
    return "linear-gradient(120deg, #f6d365 0%, #fda085 100%)"
  } else if (name === "RareWind") {
    return "linear-gradient(to top, #a8edea 0%, #fed6e3 100%)"
  } else {
    return "linear-gradient(90deg, #70e1f5 0%, #ffd194 100%)"
  }
}
</script>

<style lang="css" scoped>
  .wallpapers {
    width: 60%;
    margin-left: 20%;
    margin-top: 9%;
    margin-bottom: 7%;
    height: 400px;
    border-radius: 30px;
    background-color: rgba(255, 255, 255, 0.3);
    display: flex;
    flex-direction: column;
    align-content: center;
  }

  .wallpapers .wallpaper_btn {
    display: flex;
    position: relative;
    padding: 5px 10px;
    color: rgb(0, 0, 0, 0.8);
    font-size: 20px;
    width: 150px;
  }

  #preset, #upload, #aidraw {
    margin-left: 1%;
    margin-top: 1%;
  }

  .wallpapers .wallpaperBox .wallpaper {
    font-size: 9px;
    line-height: 200%;
  }

  .wallpapers .wallpaperBox .wallpaper ul {
    list-style: none;
  }

  .wallpaper {
    display: flex;
    justify-content: center;
  }

  #upload_img_form {
    display: inline-flex;
  }

  #upload_file {
    font-size: 18px;
  }

  #submit_wp {
    font-size: 18px;
    width: 100px;
  }

  #submit_aidraw {
    font-size: 18px;
    width: 100px;
    margin-top: 10px;
  }

  .wallpapers .wallpaperBox button {
    display: inline-block;
    padding: 10px 20px;
    margin-top: 5px;
    margin-bottom: 5px;
    border-radius: 30px;
    color: #32a3b1;
    font-size: 16px;
    text-decoration: none;
    box-shadow: -4px -4px 15px rgba(255, 255, 255, 0.8),
      4px 4px 15px rgba(0, 0, 0, .1);
    transition: 0.2s;
  }

  .wallpapers .wallpaperBox button:hover {
    box-shadow: inset -4px -4px 10px rgba(255, 255, 255, 0.5),
      inset 4px 4px 10px rgba(0, 0, 0, .1);
    transition: 0.2s;
  }

  .wallpapers .wallpaperBox .upload {
    margin: 0px 20px;
    margin-top: 20px
  }

  .wallpapers .wallpaperBox .button3 input {
    margin-top: 30px;
    margin-left: 160px;
    width: 100px;
    height: 30px;
    font-size: 18px;
    font-weight: 600;
    border: 0;
    border-radius: 5px;
    background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
  }

  .wallpaperBox {
    position: relative;
    display: flex;
    justify-content: center;
  }

  .color_wallpaper {
    width: 80px;
    height: 80px;
    display: inline-flex;
    justify-content: space-around;
    flex-direction: column;
    align-items: center;
    align-content: center;
  }

  .color_wallpaper .color_wallpaper_img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }

  .color_wallpaper .color_wallpaper_desc {
    color: rgb(0, 0, 0, 0.9);
    font-size: 12px;
  }

  .ai_wallpaper {
    display: flex;
    margin-top: 10px;
    flex-direction: column;
    align-items: center;
  }

  .prompt_form {
    box-shadow: 0 0 10px 3px #00000029;
    color: rgb(0, 0, 0, 0.9);
    backdrop-filter: blur(14px);
    background-color: rgba(255, 255, 255, 0.2);
    display: flex;
    height: 50px;
    width: 80%;
    border-radius: 40px;
    transition: 0.3s;
  }

  .prompt_form:hover {
    background-color: rgba(255, 255, 255, 0.6);
  }

  .prompt_txt {
    color: #222;
    background-color: transparent;
    font-size: 16px;
    height: 100%;
    line-height: 20px;
    border: none;
    background: none;
    outline: none;
    padding: 0 6px;
    transition: 0.2s;
    width: 100%;
    margin-left: 10px;
  }

  .highres_form {
    display: flex;
    margin-top: 10px;
    font-size: 18px;
  }

  #need_highres {
    opacity: 1;
    margin-right: 10px;
    transform: scale(1.5);
  }

  .loading_aidraw {
    display: flex;
    color: rgb(0, 0, 0, 0.9);
    padding-top: 10px;
  }

  #loading_gif {
    height: 25px;
    width: 25px;
    margin-right: 10px;
  }

  #DustyGrass {
    background: linear-gradient(90deg, #70e1f5 0%, #ffd194 100%);
  }

  #NightFade {
    background: linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%);
  }

  #WinterNeva {
    background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
  }

  #SunnyDay {
    background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
  }

  #RareWind {
    background: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  }
</style>