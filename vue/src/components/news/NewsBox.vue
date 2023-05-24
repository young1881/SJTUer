<template>
  <div class="box">
    <h3>教务信息</h3>
    <ul>
      <li>
        <a href=""
          ><span class="col1">1</span
          >[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a
        >
      </li>
      <li>
        <a href=""
          ><span class="col2">2</span
          >[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a
        >
      </li>
      <li>
        <a href=""
          ><span class="col3">3</span
          >[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a
        >
      </li>
      <li>
        <a href=""
          ><span class="col4">4</span
          >[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a
        >
      </li>
      <li>
        <a href=""
          ><span class="col5">5</span
          >[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "NewsBox",
};
</script>

<style scoped>
.box {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 250px;
  margin: 1%;
  border-radius: 2%;
  background: rgba(59, 59, 59, 0.1);
  padding: 20px;
  overflow: hidden;
}

.box h3 {
  margin: 0px;
  font: 20px;
  padding: 5px;
}

.box ul {
  margin: 0px;
  padding: 0px;
  list-style: none;
  overflow: hidden;
}

.box ul li {
  height: 30px;
  line-height: 30px;
  font-size: 16px;
  border: 1px;
  overflow: hidden;
}

.box ul li a {
  text-decoration: none;
  color: #4f4e4e;
}

.box ul li a:hover {
  color: black;
}

span {
  margin: 10px;
  font-size: 16px;
  font-weight: bold;
}

.col1 {
  color: red;
}

.col2 {
  color: #ff5c55;
}

.col3 {
  color: #ffa552;
}
</style>