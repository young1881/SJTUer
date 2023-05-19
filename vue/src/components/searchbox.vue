<template>
    <div class="search-box" id="search-box">
        <div class="search-form">
            <div class='engine-box'>
                <img class="engine" src="https://files.codelife.cc/itab/search/baidu.svg" alt="加载中">
                <i class="fa-solid fa-caret-down" style="font-size:12px; display:flex; padding: 3px 3px;"></i>
            </div>
            <input class="search-txt" id="search-text" name="search_msg" placeholder="输入文本搜索，左侧切换引擎" onkeydown="if(event.keyCode==13) document.getElementById('search-btn').click()">
            <div class='search-btn-box' id='search-btn'>
                <i class="fa-solid fa-magnifying-glass" id='search-btn-font'></i>
            </div>
        </div>
        <div class="search-engine" style="display: none;">
            <div class="search-engine-head">
                <div class="search-engine-tit">点击选择搜索引擎：</div>
            </div>
            <ul class="search-engine-list"></ul>
        </div>
    </div>
</template>

<script>
export default {
  name: 'searchbox'
}
</script>

<style scoped>

.search-engine {
    position: absolute;
    top: 60px;
    left: 0;
    width: 550px;
    background-color: rgba(255, 255, 255);
    padding: 15px 0 0 15px;
    border-radius: 30px;
    box-shadow: 0px 5px 20px 0px #d8d7d7;
    transition: all 0.3s;
    display: none;
    z-index: 999;
    box-sizing: border-box;
}

.search-engine-list::after {
    content: '';
    width: 425px;
    height: 50px;
    position: absolute;
    top: -25px;
    left: 0px;
}

.search-engine-list li {
    float: left;
    width: 140px;
    line-height: 30px;
    padding: 5px 10px 5px 10px;
    margin: 0 15px 15px 0;
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
    margin-right: 5px;
    margin-top: 2.5px;
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
    width: 550px;
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
    min-width: 60px;
    max-width: 60px;
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
    width: 450px;
}

.search-btn-box{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-width: 50px;
    max-width: 50px;
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
