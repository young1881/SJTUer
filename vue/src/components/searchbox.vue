<template>
  <div class="search-box" id="search-box">
    <!-- 搜索框 -->
    <div class="search-form">
      <!-- 搜索引擎 -->
      <div class='engine-box' @mouseover="showSearchEngine">
        <img class="engine" src="https://files.codelife.cc/itab/search/baidu.svg" alt="加载中">
        <i class="fa-solid fa-caret-down" style="font-size:12px; display:flex; padding: 3px 3px;"></i>
      </div>
      <!-- 输入框 -->
      <input class="search-txt" id="search-text" name="search_msg" placeholder="输入文本搜索，左侧切换引擎" onkeydown="if(event.keyCode==13) document.getElementById('search-btn').click()">
      <div class='search-btn-box' id='search-btn'>
        <div class="fa-solid fa-magnifying-glass" id='search-btn-font'>Go</div>
      </div>
    </div>
    <div class="search-engine" v-show="isSearchEngineShown" @mouseleave="hideSearchEngine">
      <div class="search-engine-head">
        <div class="search-engine-tit">点击选择搜索引擎：</div>
      </div>
      <ul class="search-engine-list">
        <li id="search-engine-0"><img src="https://www.baidu.com/favicon.ico"/><p>百度</p></li>
        <li id="search-engine-1"><img src="https://files.codelife.cc/itab/search/google.svg"/><p>谷歌</p></li>
        <li id="search-engine-2"><img src="https://files.codelife.cc/itab/search/bing.svg"/><p>必应</p></li>
        <li id="search-engine-3"><img src="https://files.codelife.cc/itab/search/sougou.svg"/><p>搜狗</p></li>
        <li id="search-engine-4"><img src="https://files.codelife.cc/itab/search/360.svg"/><p>360</p></li>
        <li id="search-engine-5"><img src="https://files.codelife.cc/itab/search/zhihu.svg"/><p>知乎</p></li>
        <li id="search-engine-6"><img src="https://dict.youdao.com/favicon.ico"/><p>有道</p></li>
        <li id="search-engine-7"><img src="https://so.csdn.net/favicon.ico"/><p>CSDN</p></li>
        <li id="search-engine-8"><img src="https://files.codelife.cc/itab/search/github.svg"/><p>Github</p></li>
        <li id="search-engine-9"><img src="https://files.codelife.cc/itab/search/bilibili.svg"/><p>bilibili</p></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'searchbox',
  setup(props, context) {
    const isSearchEngineShown = ref(false)
    const search = {
      data: [
        { name: '百度', url: 'https://www.baidu.com/s?wd=' },
        { name: '谷歌', url: 'https://www.google.com/search?q=' },
        { name: '必应', url: 'https://cn.bing.com/search?q=' },
        { name: '搜狗', url: 'https://www.sogou.com/web?query=' },
        { name: '360', url: 'https://www.so.com/s?q=' },
        { name: '知乎', url: 'https://www.zhihu.com/search?q=' },
        { name: '有道', url: 'https://dict.youdao.com/w/eng/' },
        { name: 'CSDN', url: 'https://so.csdn.net/so/search/s.do?q=' },
        { name: 'Github', url: 'https://github.com/search?q=' },
        { name: 'bilibili', url: 'https://search.bilibili.com/all?keyword=' },
      ]
    };

    function showSearchEngine() {
      isSearchEngineShown.value = true
      var thisSearch = 'https://www.baidu.com/s?wd=';
      var thisImg = 'https://www.baidu.com/favicon.ico';
      var searchEngineList = document.querySelectorAll('.search-engine-list li');
      searchEngineList.forEach(function (li) {
        li.addEventListener('click', function () {
          var _index = this.id.split('-')[2];
          thisImg = this.querySelector('img').getAttribute('src');
          document.querySelector('.engine').setAttribute('src', thisImg);
          thisSearch = search.data[_index].url;
          hideSearchEngine();
        });
      });
      document.querySelector('#search-btn').addEventListener('click', function () {
        var textValue = document.querySelector('#search-text').value;
        textValue = textValue.replace(/\%/g, "%25");
        textValue = textValue.replace(/\+/g, "%2B");
        textValue = textValue.replace(/\//g, "%2F");
        textValue = textValue.replace(/\?/g, "%3F");
        textValue = textValue.replace(/\&/g, "%26");
        textValue = textValue.replace(/\=/g, "%3D");
        textValue = textValue.replace(/\#/g, "%23");
        window.open(thisSearch + textValue, thisSearch + textValue);
      });
    }
    function hideSearchEngine() {
      isSearchEngineShown.value = false
    }
    return {
      isSearchEngineShown,
      showSearchEngine,
      hideSearchEngine
    }
  }
}
</script>

<style scoped>
#searchbox {
    position: absolute;
    top: 27%;
    left: 50%;
    transform: translate(-50%, -50%);
    height: 50px;
    width: 550px;
    z-index:700;
}
.search-engine {
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background-color: rgb(255, 255, 255);
    padding: 15px 0 0 15px;
    border-radius: 30px;
    box-shadow: 0px 5px 20px 0px #d8d7d7;
    transition: all 0.3s;
    z-index: 999;
    box-sizing: border-box;
}

.search-engine-list::after {
    content: '';
    width: 90%;
    height: 50px;
    position: absolute;
    top: -25px;
    left: 0px;
}

.search-engine-list li {
    float: left;
    width: 22%;
    margin: 10px 15px 10px 0;
    padding: 10px;
    background: #f9f9f9;
    color: #999999;
    cursor: pointer;
    border-radius: 10px;
    list-style: none;
    align-content: center;
}

.search-engine-list li:hover{
    background-color: rgba(0, 0, 0, 0.1);
}

.search-engine-list li p{
    font-size: 14px;
}

.search-engine-list li img {
    width: 20px;
    height: 20px;
    border-radius: 15px;
    float: left;
    max-width: 100%;
    border: 0;
}

.search-engine-head {
    overflow: hidden;
    margin-bottom: 10px;
    padding-right: 15px;
    box-sizing: border-box;
    font-size: 13px;
}

.search-engine-tit {
    float: left;
    margin: 0 10px;
    font-size: 14px;
    color: #999999;
    font-weight: 700;
    box-sizing: border-box;
}

.search-form{
    box-shadow: 0 0 10px 3px #00000029;
    color: #222;
    backdrop-filter: blur(14px);
    background-color: rgba(255, 255, 255, 0.2);
    display:flex;
    height:50px;
    width: 100%;
    border-radius: 40px;
    transition: 0.3s;
}

.search-form:hover{
    background-color: rgba(255, 255, 255, 0.6);
}

.engine-box{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-width: 10%;
    max-width: 10%;
    transition: .2s;
    position: relative;
    border-radius: 40px 0 0 40px;
}

.engine-box:hover{
    background-color: rgba(255, 255, 255, 0.8);
}

.engine {
    width: 20px;
    height: 20px;
    transition: 0.4s;
}

.search-txt {
    color: #222;
    background-color: transparent;
    font-size: 14px;
    height: 100%;
    line-height: 20px;
    border: none;
    background: none;
    outline: none;
    padding: 0 6px;
    transition: 0.2s;
    width: 80%;
}

.search-btn-box{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-width: 10%;
    max-width: 10%;
    position: relative;
    transition: 0.4s;
    border-radius: 0 40px 40px 0;
}

.search-btn-box:hover{
    background-color: rgba(255, 255, 255, 0.8);
}

#search-btn-font{
    font-size:20px;
}

input::-webkit-input-placeholder {
    color: #555;
  }
  input::-moz-input-placeholder {
    color: #555;
  }
  input::-ms-input-placeholder {
    color: #555;
  }
</style>
