<template>
  <div class="wallpapers" id="wallpapers">
    <div class="card">
      <button class="wallpaper_btn active">预设壁纸</button>
      <button class="wallpaper_btn">自主上传</button>
      <div class="wallpaperBox">
        <div class="wallpaper show">
          <div class="color_wallpaper_all">
            <div class="color_wallpaper">
              <div class="color_wallpaper_img" id="DustyGrass" onclick="change_color_wallpaper(this)"></div>
              <div class="color_wallpaper_desc">Dusty Grass</div>
            </div>
            <div class="color_wallpaper">
              <div class="color_wallpaper_img" id="NightFade" onclick="change_color_wallpaper(this)"></div>
              <div class="color_wallpaper_desc">Night Fade</div>
            </div>
            <div class="color_wallpaper">
              <div class="color_wallpaper_img" id="WinterNeva" onclick="change_color_wallpaper(this)"></div>
              <div class="color_wallpaper_desc">Winter Neva</div>
            </div>
            <div class="color_wallpaper">
              <div class="color_wallpaper_img" id="SunnyDay" onclick="change_color_wallpaper(this)"></div>
              <div class="color_wallpaper_desc">Sunny Day</div>
            </div>
            <div class="color_wallpaper">
              <div class="color_wallpaper_img" id="RareWind" onclick="change_color_wallpaper(this)"></div>
              <div class="color_wallpaper_desc">Rare Wind</div>
            </div>
          </div>
          <div class = "button4">
            <a href = "javascript:void(0)" onclick = "closeWallpaperDialog()">点我关闭</a>
          </div>
        </div>
        <div class="wallpaper">
          <form id="upload_img_form">
            <div class="upload">
              <input type="file" name="upload_file" id="upload_file">
            </div>
            <div class="button3">
              <a href = "javascript:void(0)" onclick = "upload_img()">
                <input type="submit" value="提 交">
              </a>
            </div>
            <div class = "button5">
              <a href = "javascript:void(0)" onclick = "closeWallpaperDialog()">点我关闭</a>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'aibackground'
}
</script>

<style lang="css">
.wallpapers {
  display: none;
  justify-content: space-around;
  top: 40%;
  left: 35%;
  width: 420px;
  z-index: 5000;
  height: 180px;
  padding: 20px;
  position: absolute;
  flex-wrap: wrap;
  align-items: center;
  border-radius: 40px;
  background-color: rgba(0, 0, 0, 0.8);
  opacity: 0.9;
  backdrop-filter: blur(4px);
}

.wallpapers .card .wallpaper_btn{
  display: inline-block;
  padding: 5px 10px;
  margin-bottom: 10px;
  border-radius: 20px;
  color: floralwhite;
  font-size: 12px;
  background-color: transparent;
  border-width: 0;
}

.wallpapers .card .wallpaper_btn.active{
  background-color: rgba(255, 255, 255, 0.2);
  opacity: 1;
}

.wallpapers .card .wallpaperBox .wallpaper{
  font-size: 9px;
  line-height: 200%;
  display: none;
}

.wallpapers .card .wallpaperBox .wallpaper ul{
  list-style: none;
}

.wallpapers .card .wallpaperBox .wallpaper.show{
  color: white;
  line-height: 200%;
  list-style: none;
  font-size: 9px;
  display: flex;
  flex-wrap: wrap;
}

.wallpapers .card .wallpaperBox .wallpaper.show ul{
  list-style: none;
}

.wallpapers .card .wallpaperBox button {
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

.wallpapers .card .wallpaperBox button:hover {
  box-shadow: inset -4px -4px 10px rgba(255, 255, 255, 0.5),
  inset 4px 4px 10px rgba(0, 0, 0, .1);
  transition: 0.2s;
}

.wallpapers .card .wallpaperBox .upload{
  margin: 0px 20px;
  margin-top: 20px
}

.wallpapers .card .wallpaperBox .button3 input{
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

.wallpapers .card .wallpaperBox .button4{
  margin: 0 auto;
  margin-top: 40px;
}

.wallpapers .card .wallpaperBox .button4 a{
  color:#ffffff99;
  font-size: 15px;
}

.wallpapers .card .wallpaperBox .button5{
  margin: 0px 180px;
  margin-top: 15.5px;
}

.wallpapers .card .wallpaperBox .button5 a{
  color:#ffffff99;
  font-size: 15px;
}

.color_wallpaper_all{
  align-content: center;
  position: absolute;
}

.color_wallpaper{
  width:80px;
  height:80px;
  display: inline-flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
  align-content: center;
}

.color_wallpaper .color_wallpaper_img{
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.color_wallpaper .color_wallpaper_desc{
  color: white;
  font-size: 8px;
}

#DustyGrass {
  background: linear-gradient(90deg, #70e1f5 0%, #ffd194 100%);
}

#NightFade {
  background: linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%);
}

#WinterNeva{
  background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
}

#SunnyDay {
  background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
}

#RareWind {
  background: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
}
</style>
