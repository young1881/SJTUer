<template>
  <div id="app">
    <div id="head">
      <div class="change" :class="{ active: simple === true }" v-if="islogin">
        <flip-clock @click="changeSimple"></flip-clock>
        <searchbox id="searchbox"></searchbox>
      </div>
      <div class="change1" :class="{ active: simple === true }" v-if="!islogin">
        <flip-clock @click="changeSimple"></flip-clock>
        <searchbox id="searchbox"></searchbox>
      </div>
      <!--transition name="move">
        <div v-if="isshowing">
          <flip-clock @click="changeSimple"></flip-clock>
          <searchbox id="searchbox"></searchbox>
        </div>
      </transition-->
      <!--div id="box">
        <flip-clock @click="changeSimple"></flip-clock>
        <searchbox id="searchbox"></searchbox>
      </div-->
      <charts
        id="charts"
        v-if="showcomponent === 'charts' && dataFlag"
        :library="library"
        :canteen="canteen"
      ></charts>
      <!--div class="loading">
        <p v-if="showcomponent === 'charts' && !dataFlag">LOADING...</p>
      </div-->
    </div>

    <websites
      id="websites"
      v-if="showcomponent === 'websites'"
      :sites="sites"
    ></websites>
    <todo-app
      :simple="simple"
      v-if="(showcomponent === 'todo' || showcomponent === 'simpletodo') && islogin"
    ></todo-app>
    <news-column
      v-if="showcomponent === 'news' && scrapyFlag"
      :jwc="jwc"
      :jnews="jnews"
      :weibo="weibo"
      :zhihu="zhihu"
      :bilibili="bilibili"
    ></news-column>
    <weather v-if="showcomponent === 'weather'"></weather>
    <aibackground v-if="showcomponent === 'aibackground'"></aibackground>
    <sidebar @ChangeComponent="ChangeComponent"></sidebar>
    <poem v-if="scrapyFlag" :poem="poem"></poem>
  </div>
</template>

<script>
import FlipClock from "./components/FlipClock.vue";
import Searchbox from "./components/searchbox.vue";
import Sidebar from "./components/sidebar.vue";
import websites from "./components/websites.vue";
import charts from "./components/charts.vue";
import TodoApp from "./components/todolist/TodoApp.vue";
import NewsColumn from "./components/news/NewsColumn.vue";
import { getview, getscrapy, getdata } from "./api/api.js";
import { ref, onMounted, watch } from "vue";
import poem from "./components/poem.vue";
import weather from "./components/weather.vue";
import aibackground from "./components/aibackground.vue";

export default {
  components: {
    FlipClock,
    websites,
    Searchbox,
    Sidebar,
    charts,
    poem,
    TodoApp,
    NewsColumn,
    weather,
    aibackground,
  },
  name: "App",
  setup() {
    let simple = ref(false);
    let isshowing = true;
    const sites = ref([]);
    let showcomponent = ref("websites");
    let lastcomponent = ref("websites");
    const library = ref([]);
    const canteen = ref([]);
    const jwc = ref([]);
    const jnews = ref([]);
    const weibo = ref([]);
    const zhihu = ref([]);
    const bilibili = ref([]);
    const poem = ref([]);
    const wallpaper = ref([])
    const scrapyFlag = ref(false);
    const dataFlag = ref(false);
    const islogin = ref(false)

    const getView = async () => {
      const response = await getview();
      sites.value = response.data["sites"];
      // 从后端数据库获取的todolist数据，直接存到本地
      localStorage.setItem(
        "todos",
        JSON.stringify(response.data["task"]),
        null,
        2
      );

    setTimeout(() => {
      if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) islogin.value = false
      else {
        islogin.value = true
      }
    }, 300)

      wallpaper.value = response.data["wallpaper"]
      console.log(wallpaper.value);
      const body = document.querySelector('body');
      if (wallpaper.value.css)
        body.style.background = wallpaper.value.css;
      else
        body.setAttribute('style', 'background-image: url("http://127.0.0.1:8000/' + wallpaper.value.photo_url + '");');

      sessionStorage.setItem("name", response.data["name"]);
      sessionStorage.setItem("jaccount", response.data["account"]);
    };

    const getScrapy = async () => {
      const response = await getscrapy();
      jwc.value = response.data["jwc"];
      jnews.value = response.data["jnews"];
      weibo.value = response.data["weibo"];
      zhihu.value = response.data["zhihu"];
      bilibili.value = response.data["bilibili"];
      poem.value = response.data["poem"];
      scrapyFlag.value = true;
    };

    const getData = async () => {
      const response = await getdata();
      library.value = response.data["library"];
      canteen.value = response.data["canteen"];
      dataFlag.value = true;
    };

    const ChangeComponent = (component) => {
      showcomponent.value = component;
      simple.value = false;
    };

    const printData = () => {
      //console.log(this.show)
    };
    const changeSimple = () => {
      if (showcomponent.value === "simpletodo") {
        showcomponent.value = lastcomponent.value;
        simple.value = false;
      } else {
        lastcomponent.value = showcomponent.value;
        showcomponent.value = "simpletodo";
        simple.value = true;
      }

      //console.log(simple.value);
    };

    onMounted(() => {
      getView();
      printData();
      getScrapy();
    });

    watch(
      () => showcomponent.value,
      (newVal, oldVal) => {
        if (newVal === "charts") {
          getData();
        }
        if (newVal === "news") {
          getScrapy();
        }
      }
    );

    return {
      isshowing,
      simple,
      sites,
      library,
      canteen,
      jwc,
      jnews,
      weibo,
      zhihu,
      bilibili,
      poem,
      islogin,
      getView,
      getScrapy,
      getData,
      printData,
      showcomponent,
      ChangeComponent,
      scrapyFlag,
      dataFlag,
      TodoApp,
      NewsColumn,
      changeSimple,
      lastcomponent,
    };
  },
};
</script>


<style>
html {
  margin: 0 auto;
  padding: 0;
  height: 100%;
}

body {
  background: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  background-size: cover;
  z-index: -3;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  margin: 0 auto;
  padding: 0;
}

#head {
  margin-top: 4%;
  background-color: rgba(165, 42, 42, 0);
}

.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font: bold;
  font-size: 60px;
  color: black;
}

.change {
  transition: 0.5s;
}
.change.active {
  margin-top: 10%;
  transition: 0.5s;
}

.change1 {
  transition: 0.5s;
}
.change1.active {
  margin-top: 18%;
  transition: 0.5s;
}



</style>