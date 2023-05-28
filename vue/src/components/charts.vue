<template>
    <div class="charts">
        <e-charts class="library" :option="liboption" />
        <e-charts class="canteen" :option="canteenoption" />
    </div>
</template>

<script setup>
    import { ref, computed, toRefs, watch } from 'vue';
    import { defineProps } from 'vue';

    const props = defineProps({
        library: {
            type: Array,
            required: true,
        },
        canteen: {
            type: Array,
            required: true,
        }
    });

    const { library, canteen } = toRefs(props);

    console.log(library.value[0]);
    //value1代表餐厅已有人数，value2代表餐厅还可以容纳的人数
    const CanteenData = ref([
        { value1: canteen.value[0].Seat_u, value2: canteen.value[0].Seat_r, name: '一餐' },
        { value1: canteen.value[1].Seat_u, value2: canteen.value[1].Seat_r, name: '二餐' },
        { value1: canteen.value[2].Seat_u, value2: canteen.value[2].Seat_r, name: '三餐' },
        { value1: canteen.value[3].Seat_u, value2: canteen.value[3].Seat_r, name: '四餐' },
        { value1: canteen.value[4].Seat_u, value2: canteen.value[4].Seat_r, name: '五餐' },
        { value1: canteen.value[5].Seat_u, value2: canteen.value[5].Seat_r, name: '六餐' },
        { value1: canteen.value[6].Seat_u, value2: canteen.value[6].Seat_r, name: '七餐' },
        { value1: canteen.value[7].Seat_u, value2: canteen.value[7].Seat_r, name: '哈乐' },
    ]);
    //value1代表图书馆已有人数，value2代表图书馆还可以容纳的人数
    const LibraryData = ref([
        { value1: library.value[0].inCounter, value2: library.value[0].max - library.value[0].inCounter, name: '图书馆主馆' },
        { value1: library.value[1].inCounter, value2: library.value[1].max - library.value[1].inCounter, name: '李政道图书馆' },
        { value1: library.value[2].inCounter, value2: library.value[2].max - library.value[2].inCounter, name: '包玉刚图书馆' },
        { value1: library.value[3].inCounter, value2: library.value[3].max - library.value[3].inCounter, name: '徐汇社科馆' },
    ]);


    const liboption = computed(() => {
        return {
            color: [
                '#d7ab82','#d87c7c'
            ],
            title: {
                text: '图书馆人流量统计',
                x: 'center',
                y: 'top'
            },
            //悬停提示已有人数和可容纳人数
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            //侧边栏，可以实现看数据表，bar和stack相互转换,下载图片
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
            //图例
            legend: {
                orient: 'horizontal',
                x: 'right]',
                y: 'top',
            },
            xAxis: {
                type: 'category',
                data: LibraryData.value.map(d => d.name),
                "axisLabel": { interval: 0 }
            },
            yAxis: {
                type: 'value',
            },
            series: [
                {
                    name: "在馆人数",
                    data: LibraryData.value.map(d => d.value1),
                    type: 'bar',
                },
                {
                    name: "可容纳人数",
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
                x: 'center',
                y: 'top',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
             //侧边栏，可以实现看数据表，bar和stack相互转换,下载图片
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
             //图例
            legend: {
                orient: 'horizontal',
                x: 'right',
                y: 'top',
            },
            xAxis: {
                type: 'category',
                data: CanteenData.value.map(d => d.name),
                "axisLabel": { interval: 0 }
            },
            yAxis: {
                type: 'value',
            },
            series: [
                {
                    name: "已有人数",
                    data: CanteenData.value.map(d => d.value1),
                    type: 'bar',
                },
                {
                    name: "可容纳人数",
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
        margin-left: 10%;
        margin-top: 9%;
        height: 400px;
        margin-bottom: 7%;
        background-color: rgba(255, 255, 255, 0.508);
        border-radius: 30px;
        display: flex;
        align-content: center;
    }

    .library {
        width: 50%;
        height: 400px;
        border-radius: 30px;
        margin-top: 3%;
        margin-left: 3%;
        display: inline-block;
        align-content: center;
    }

    .canteen {
        width: 50%;
        height: 400px;
        margin-top: 3%;
        margin-right: 3%;
        display: inline-block;
        border-radius: 30px;
        align-content: center;
    }
</style>