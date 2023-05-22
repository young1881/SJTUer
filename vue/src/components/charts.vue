<template>
    <div class="charts">
        <e-charts class="library" :option="liboption" />
        <e-charts class="canteen" :option="canteenoption"/>
    </div>
</template>
  
<script setup>
    import { ref, computed } from 'vue';
    const CanteenData = ref([
        { value1: 0, value2: 0, name: '一餐' },
        { value1: 0, value2: 0, name: '一餐清真' },
        { value1: 0, value2: 0, name: '二餐' },
        { value1: 0, value2: 0, name: '三餐' },
        { value1: 0, value2: 0, name: '三餐清真' },
        { value1: 0, value2: 0, name: '四餐' },
        { value1: 0, value2: 0, name: '五餐' },
        { value1: 0, value2: 0, name: '哈乐' },
        { value1: 0, value2: 0, name: '玉兰苑' },
    ]);

    const LibraryData = ref([
        { value1: 0, value2: 0, name: '图书馆主馆' },
        { value1: 0, value2: 0, name: '李政道图书馆' },
        { value1: 0, value2: 0, name: '包玉刚图书馆' },
        { value1: 0, value2: 0, name: '徐汇社科馆' },
    ]);

    setInterval(() => {
        CanteenData.value = CanteenData.value.map(item => ({
        ...item,
        value1: 100,
        }));
    }, 5000);
    
    setInterval(() => {
        CanteenData.value = CanteenData.value.map(item => ({
        ...item,
        value2: Math.random() * 100,
        }));
    }, 5000);

    setInterval(() => {
        LibraryData.value = LibraryData.value.map(item => ({
        ...item,
        value1: Math.random() * 100,
        }));
    }, 5000);

    setInterval(() => {
        LibraryData.value = LibraryData.value.map(item => ({
        ...item,
        value2: Math.random() * 100,
        }));
    }, 5000);


    const liboption = computed(() => {
        return {
            color: [
                '#d7ab82','#d87c7c','#4b565b','#724e58','#cc7e63','#787464','#efa18d','#6e7074',
            ],
            title: {
                text: '图书馆人流量统计',
                x:'center',
                y:'top'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'shadow'
                }   
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
                }
            },
            legend: {
                orient: 'horizontal',
                x:'right]',
                y:'top',
            },
            xAxis: {
                type: 'category',
                data: LibraryData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },
            series: [
            {
                name:"在馆人数",
                data: LibraryData.value.map(d => d.value1),
                type: 'bar',
            },
            {
                name:"可容纳人数",
                data: LibraryData.value.map(d => d.value2),
                type: 'bar',
            },
            ],
        }
    });
  
    const canteenoption = computed(() => {
        return {
            title: {
                text: '餐厅人流量统计',
                x:'center',
                y:'top',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'shadow'
                }   
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
                }
            },
            legend: {
                orient: 'horizontal',
                x:'right',
                y:'top',
            },
            xAxis: {
                type: 'category',
                data: CanteenData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },
            series: [
            {
                name:"已有人数",
                data: CanteenData.value.map(d => d.value1),
                type: 'bar',
            },
            {
                name:"可容纳人数",
                data: CanteenData.value.map(d => d.value2),
                type: 'bar',
            },
            ],
        }
    });
</script>
  
<style scoped>
  .charts {
    width: 80%;
    margin-left:10%;
    margin-top: 7%;
    height: 400px;
    margin-bottom: 7%;
    background-color: rgba(255, 255, 255, 0.304);
    border-radius: 30px;
    display: flex;
    align-content: center;
  }
  .library{
    width: 50%;
    height: 400px;
    border-radius: 30px;
    margin-top: 3%;
    margin-left: 3%;
    display: inline-block;
    align-content: center;
  }
  .canteen{
    width: 50%;
    height: 400px;
    margin-top: 3%;
    margin-right: 3%;
    display: inline-block; 
    border-radius: 30px;
    align-content: center;
  }
  </style>