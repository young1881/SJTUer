<template>
  <div class="optionfilter">
    <select-data
      :selectData="Priority"
      :selValue="PriorityValue"
      color="green"
      @getValue="getPrio"
    />
    <select-data
      :selectData="Category"
      :selValue="CategoryValue"
      color="green"
      @getValue="getCate"
    />
    <select-data
      :selectData="Timeslice"
      :selValue="TimesliceValue"
      color="green"
      @getValue="getTime"
    />
    <!--input  class="filt" type="submit" value="Filt" @click="optionfilt" -->
    <button class="filt" @click="optionfilt">Filt</button>
  </div>
</template>

<script>
import SelectData from "./SelectData.vue";
//import { ref } from "vue";
export default {
  name: "OptionFilter",
  components: { SelectData },
  setup(props, context) {
    const Priority = [
      {
        name: "All",
        value: "All",
      },
      {
        name: "Low",
        value: "Low",
      },
      {
        name: "Medium",
        value: "Medium",
      },
      {
        name: "High",
        value: "High",
      },
    ];
    const Category = [
      {
        name: "All",
        value: "All",
      },
      {
        name: "School",
        value: "School",
      },
      {
        name: "Home",
        value: "Home",
      },
    ];
    const Timeslice = [
      {
        name: "All",
        value: "All",
      },
      {
        name: "5min",
        value: "5min",
      },
      {
        name: "25min",
        value: "25min",
      },
      {
        name: "1h",
        value: "1h",
      },
      {
        name: "2h",
        value: "2h",
      },
      {
        name: ">2h",
        value: ">2h",
      },
    ];

    let Prio = "All";
    let Cate = "All";
    let Time = "All";

    const PriorityValue = Priority[0].value;
    const CategoryValue = Category[0].value;
    const TimesliceValue = Timeslice[0].value;

    const getPrio = (name) => {
      Prio = name;
      //console.log("item:", name, value, index);
    };
    const getCate = (name) => {
      Cate = name;
    };
    const getTime = (name) => {
      Time = name;
    };
    const optionfilt = () => {
      console.log(Prio);
      console.log(Cate);
      console.log(Time);

      context.emit("option-filt", Prio, Cate, Time);
    };
    return {
      Priority,
      Category,
      Timeslice,
      PriorityValue,
      CategoryValue,
      TimesliceValue,
      getPrio,
      getCate,
      getTime,
      optionfilt,
    };
  },
};
</script>

<style>
.optionfilter {
  display: grid;
  margin-left: auto;
  grid-template-columns: 100px 100px 100px auto;
  grid-gap: 30px;
  margin-bottom: 20px;
}

.optionfilter .filt {
  appearance: none;
  border: none;
  outline: none;
  display: flex;
  margin-left: auto;
  height: 40px;
  width: 100px;
  font-size: 16px;
  padding: 8px 16px;
  text-align: center;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  font-weight: 700;
  background-color: rgba(255, 255, 255, 0.8);
}

.optionfilter .filt:hover {
  background-color: rgba(227, 227, 227, 0.8);
  cursor: pointer;
}
</style>