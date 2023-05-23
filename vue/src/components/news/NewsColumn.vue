<template>
  <div class="column">
    <div class="box">
      <div class="smallbox">
        <h3>教务信息</h3>
        <ul>
          <li><a :href="jwc[0].url" target="_blank"><span class="col1">1</span>{{ jwc[0].title }}</a></li>
          <li><a :href="jwc[1].url" target="_blank"><span class="col2">2</span>{{ jwc[1].title }}</a></li>
          <li><a :href="jwc[2].url" target="_blank"><span class="col3">3</span>{{ jwc[2].title }}</a></li>
          <li><a :href="jwc[3].url" target="_blank"><span class="col4">4</span>{{ jwc[3].title }}</a></li>
          <li><a :href="jwc[4].url" target="_blank"><span class="col5">5</span>{{ jwc[4].title }}</a></li>
          <li><a :href="jwc[5].url" target="_blank"><span class="col6">6</span>{{ jwc[5].title }}</a></li>
          <li><a :href="jwc[6].url" target="_blank"><span class="col7">7</span>{{ jwc[6].title }}</a></li>
          <li><a :href="jwc[7].url" target="_blank"><span class="col8">8</span>{{ jwc[7].title }}</a></li>
          <li><a :href="jwc[8].url" target="_blank"><span class="col9">9</span>{{ jwc[8].title }}</a></li>
          <!--li><a :href="jwc[9].url" target="_blank"><span class = "col10">10</span>{{ jwc[9].title }}</a></li-->
        </ul>
      </div>
      <div class="smallbox">
        <h3>交大新闻</h3>
        <ul>
          <li><a :href="jnews[0].url" target="_blank"><span class="col1">1</span>{{ jnews[0].title }}</a></li>
          <li><a :href="jnews[1].url" target="_blank"><span class="col2">2</span>{{ jnews[1].title }}</a></li>
          <li><a :href="jnews[2].url" target="_blank"><span class="col3">3</span>{{ jnews[2].title }}</a></li>
          <li><a :href="jnews[3].url" target="_blank"><span class="col4">4</span>{{ jnews[3].title }}</a></li>
          <li><a :href="jnews[4].url" target="_blank"><span class="col5">5</span>{{ jnews[4].title }}</a></li>
          <li><a :href="jnews[5].url" target="_blank"><span class="col6">6</span>{{ jnews[5].title }}</a></li>
          <li><a :href="jnews[6].url" target="_blank"><span class="col7">7</span>{{ jnews[6].title }}</a></li>
          <li><a :href="jnews[7].url" target="_blank"><span class="col8">8</span>{{ jnews[7].title }}</a></li>
          <li><a :href="jnews[8].url" target="_blank"><span class="col9">9</span>{{ jnews[8].title }}</a></li>
          <!--li><a href=""><span class = "col10">10</span>[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a></li-->
        </ul>
      </div>
      <div class="smallbox">
        <div class="head">
          <h3 :class="{ active: news === 'weibo' }" @click="news='weibo'">微博热搜</h3>
          <h3 :class="{ active: news === 'zhihu' }" @click="news='zhihu'">知乎</h3>
          <h3 :class="{ active: news=== 'bilibili' }" @click="news='bilibili'">b站</h3>
        </div>
        <ul v-if="news==='weibo'&& weibo.length > 1">
          <li><a :href="weibo[0].url" target="_blank"><span class="col1">1</span>{{ weibo[0].name }}</a></li>
          <li><a :href="weibo[1].url" target="_blank"><span class="col2">2</span>{{ weibo[1].name }}</a></li>
          <li><a :href="weibo[2].url" target="_blank"><span class="col3">3</span>{{ weibo[2].name }}</a></li>
          <li><a :href="weibo[3].url" target="_blank"><span class="col4">4</span>{{ weibo[3].name }}</a></li>
          <li><a :href="weibo[4].url" target="_blank"><span class="col5">5</span>{{ weibo[4].name }}</a></li>
          <li><a :href="weibo[5].url" target="_blank"><span class="col6">6</span>{{ weibo[5].name }}</a></li>
          <li><a :href="weibo[6].url" target="_blank"><span class="col7">7</span>{{ weibo[6].name }}</a></li>
          <li><a :href="weibo[7].url" target="_blank"><span class="col8">8</span>{{ weibo[7].name }}</a></li>
          <li><a :href="weibo[8].url" target="_blank"><span class="col9">9</span>{{ weibo[8].name }}</a></li>
          <!--li><a href=""><span class = "col10">10</span>[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a></li-->
        </ul>
        <ul v-else-if="news==='weibo'">
          <li>{{ weibo[0].name }}</li>
        </ul>

        <ul v-if="news==='zhihu'&& zhihu.length > 1">
          <li><a :href="zhihu[0].url" target="_blank"><span class="col1">1</span>{{ zhihu[0].name }}</a></li>
          <li><a :href="zhihu[1].url" target="_blank"><span class="col2">2</span>{{ zhihu[1].name }}</a></li>
          <li><a :href="zhihu[2].url" target="_blank"><span class="col3">3</span>{{ zhihu[2].name }}</a></li>
          <li><a :href="zhihu[3].url" target="_blank"><span class="col4">4</span>{{ zhihu[3].name }}</a></li>
          <li><a :href="zhihu[4].url" target="_blank"><span class="col5">5</span>{{ zhihu[4].name }}</a></li>
          <li><a :href="zhihu[5].url" target="_blank"><span class="col6">6</span>{{ zhihu[5].name }}</a></li>
          <li><a :href="zhihu[6].url" target="_blank"><span class="col7">7</span>{{ zhihu[6].name }}</a></li>
          <li><a :href="zhihu[7].url" target="_blank"><span class="col8">8</span>{{ zhihu[7].name }}</a></li>
          <li><a :href="zhihu[8].url" target="_blank"><span class="col9">9</span>{{ zhihu[8].name }}</a></li>
          <!--li><a href=""><span class = "col10">10</span>[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a></li-->
        </ul>
        <ul v-else-if="news==='zhihu'">
          <li>{{ zhihu[0].name }}</li>
        </ul>

        <ul v-if="news==='bilibili'&& bilibili.length > 1">
          <li><a :href="bilibili[0].url" target="_blank"><span class="col1">1</span>{{ bilibili[0].title }}</a></li>
          <li><a :href="bilibili[1].url" target="_blank"><span class="col2">2</span>{{ bilibili[1].title }}</a></li>
          <li><a :href="bilibili[2].url" target="_blank"><span class="col3">3</span>{{ bilibili[2].title }}</a></li>
          <li><a :href="bilibili[3].url" target="_blank"><span class="col4">4</span>{{ bilibili[3].title }}</a></li>
          <li><a :href="bilibili[4].url" target="_blank"><span class="col5">5</span>{{ bilibili[4].title }}</a></li>
          <li><a :href="bilibili[5].url" target="_blank"><span class="col6">6</span>{{ bilibili[5].title }}</a></li>
          <li><a :href="bilibili[6].url" target="_blank"><span class="col7">7</span>{{ bilibili[6].title }}</a></li>
          <li><a :href="bilibili[7].url" target="_blank"><span class="col8">8</span>{{ bilibili[7].title }}</a></li>
          <li><a :href="bilibili[8].url" target="_blank"><span class="col9">9</span>{{ bilibili[8].title }}</a></li>
          <!--li><a href=""><span class = "col10">10</span>[主题教育]上海交大主题教育专题读书班举办黄大年同志先进事迹报告会</a></li-->
        </ul>
        <ul v-else-if="news==='bilibili'">
          <li>{{ bilibili[0].title }}</li>
        </ul>

      </div>
    </div>
  </div>
</template>

<script>
  //import NewsBox from "./NewsBox.vue";
  import { ref } from 'vue';
  export default {
    name: "NewsColumn",
    components: { ref },
    props: {
      jwc: {
        type: Array,
        required: true
      },
      jnews: {
        type: Array,
        required: true
      },
      weibo: {
        type: Array,
        required: true
      },
      zhihu: {
        type: Array,
        required: true
      },
      bilibili: {
        type: Array,
        required: true
      }
    },
    setup() {
      let news = ref('weibo');
      return {
        news,
      }
    }
  }
</script>

<style>
  .column {
    display: flex;
    justify-content: center;
    align-items: center;
    background: none;
  }

  .box {
    margin: auto;
    margin-top: 120px;
    padding: 10px;
    width: 80%;
    height: 300px;
    background-color: none;
    border-radius: 30px;
    display: flex;
    flex-wrap: wrap;
    align-content: start;
    align-items: flex-start;
  }

  .smallbox {
    display: flex;
    flex-direction: column;
    width: 30%;
    margin: 1.5%;
    border-radius: 2%;
    background: rgba(255, 255, 255, 0.5);
    padding: 20px;
    overflow: hidden;
  }

  .smallbox .head {
    display: flex;
  }

  .smallbox h3 {
    margin: 0px;
    font: 20px;
    padding: 10px;
    color: black;
  }

  .smallbox .head h3 {
    color: #717171;
    cursor: pointer;
  }

  .smallbox .head h3.active {
    color: black;
    cursor: pointer;
  }

  .smallbox ul {
    margin: 0px;
    padding: 0px;
    list-style: none;
    overflow: hidden;
  }

  .smallbox ul li {
    height: 30px;
    line-height: 30px;
    font-size: 17px;
    border: 1px;
    overflow: hidden;
    margin: 0px;
  }

  .smallbox ul li a {
    text-decoration: none;
    color: #4f4e4e;
  }

  .smallbox ul li a:hover {
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