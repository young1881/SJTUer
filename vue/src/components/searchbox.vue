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
        <div class="fa-solid fa-magnifying-glass" id='search-btn-font'>
          <svg t="1684771162366" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="16262" width="32" height="32"><path d="M688.4 420.6c0-71.2-27.7-138.2-78.1-188.5C560 181.7 493 154 421.8 154c-2.7 0-5.4 0.1-8.1 0.1-29.6 14.1-57.3 33.3-81.8 57.8-115.2 115.2-115.2 302.1 0 417.3 24.7 24.7 52.6 44 82.5 58.2 70.7 2 141.9-24.3 196-78.3 50.3-50.4 78-117.3 78-188.5z" fill="#91B4FF" p-id="16263"></path><path d="M421.4 744.5c-78.4 0-156.8-28.5-219.1-85.8-11.6-10.7-12.3-28.7-1.6-40.2 10.7-11.6 28.7-12.3 40.2-1.6 105.5 97.2 267.6 93.8 369.1-7.7 50.4-50.4 78.1-117.3 78.1-188.5S660.4 282.5 610 232.2 492.7 154 421.5 154 283.3 181.7 233 232.1c-56 56-84.1 133.4-77 212.4 1.4 15.7-10.2 29.5-25.8 30.9-15.6 1.3-29.5-10.2-30.9-25.8-8.6-95.8 25.5-189.8 93.5-257.7 126.2-126.2 331.4-126.2 457.6 0 126.2 126.2 126.2 331.4 0 457.6-63.4 63.2-146.2 95-229 95z" fill="#3778FF" p-id="16264"></path><path d="M169.3 601.8c-9.6 0-19-4.9-24.4-13.7-4.6-7.5-8.8-15.2-12.7-23-5.1-10.1-9.6-20.7-13.6-31.4-5.5-14.7 2-31.1 16.7-36.6s31.1 2 36.6 16.7c3.3 8.8 7 17.4 11.2 25.8 3.2 6.4 6.7 12.7 10.4 18.9 8.2 13.4 3.9 31-9.6 39.1-4.5 2.9-9.6 4.2-14.6 4.2zM913.1 911.9c-15.3 15.3-40.4 15.3-55.7 0l-261-261c-0.4-0.4-0.4-1 0-1.4l54.3-54.3c0.4-0.4 1-0.4 1.4 0l261 261c15.4 15.3 15.4 40.4 0 55.7z" fill="#3778FF" p-id="16265"></path></svg>
        </div>
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
