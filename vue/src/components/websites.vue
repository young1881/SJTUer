<template>
  <div class="websites">
    <div class = "sitebox">
        <site></site><site></site><site></site><site></site><site></site><site></site><site></site><site></site>
    </div>
  </div>
</template>

<script>
import site from './site.vue'
export default {
  components: { site },
  name: 'websites'
}
</script>

<style>
.websites{
  display: flex;
  justify-content: center;
  align-items: center;

}
.sitebox{
  margin: 10%;
  padding: 10px;
  width: 40%;
  height: 300px;
  background-color: rgb(255,255,255,0.5);
  border-radius: 30px;
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
</style>
