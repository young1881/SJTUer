<template>
  <div class="sitesmallbox">
    <a :href="siteUrl" target="_blank" >
      <div class="img">
        <img :src="siteSrc">
      </div>
    </a>
    <p >{{ siteName }}</p>
  </div>
</template>

<script>
export default {
  name: 'site',
  props: {
    siteUrl: String,
    siteSrc: String,
    siteName: String
  }
}
</script>

<style>
.sitesmallbox {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  width: 80px;
  height: 100px;
  margin: 10px 20px;
}

.sitesmallbox .img {
  width: 70px;
  height: 70px;
  background-color: rgb(255, 255, 255,0.5);
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

</style>
