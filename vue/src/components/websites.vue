<template>
  <div class="websites">
    <div class = "sitebox">
        网站组件显示
    </div>
  </div>
</template>

<script>
export default {
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
    margin: 5%;
    width: 500px;
    height: 300px;
    background-color: rgb(252, 251, 208);
    border-radius: 10px;
}

</style>
