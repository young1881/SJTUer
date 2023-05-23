<template>
  <div class="newtodo">
    <input type="text" class="name" v-model="todoName" placeholder="e.g Homework" />
    <div class="optionline">
      <!--
      <input type="text" class="option" placeholder="priority" />
      <input type="text" class="option" placeholder="category" />
      <input type="text" class="option" placeholder="timeslice" />
      !-->
      <select-data :selectData="Priority" :selValue="PriorityValue" color='green' @getValue="getPrio" />
      <select-data :selectData="Category" :selValue="CategoryValue" color='green' @getValue="getCate" />
      <select-data :selectData="Timeslice" :selValue="TimesliceValue" color='green' @getValue="getTime" />
      <input type="submit" value="Add Todo" @click="submitNewtodo" />
    </div>
  </div>
</template>

<script>
  import { ref } from "vue";
  import SelectData from "./SelectData.vue";
  export default {
    components: { SelectData },
    name: "NewTodo",

    setup(props, context) {
      /*
      const todoPriority = ref("LOW");
      const todoCategory = ref("HOME");
      const todoTimeslice = ref("5MIN");
      */
      const todoName = ref("");
      const Priority = [
        {
          name: "Low",
          value: 1,
        },
        {
          name: "Medium",
          value: 2,
        },
        {
          name: "High",
          value: 3,
        },
      ];
      const Category = [
        {
          name: "School",
          value: 1,
        },
        {
          name: "Home",
          value: 2,
        },
      ];
      const Timeslice = [
        {
          name: "5min",
          value: 1,
        },
        {
          name: "25min",
          value: 2,
        },
        {
          name: "1h",
          value: 3,
        },
        {
          name: "2h",
          value: 4,
        },
        {
          name: ">2h",
          value: 5,
        },
      ];
      const todoDone = ref < Boolean > "false";
      let Prio = { name: "Low", value: 1 };
      let Cate = { name: "School", value: 1 };
      let Time = { name: "5min", value: 1 };
      const PriorityValue = Priority[0].value;
      const CategoryValue = Category[0].value;
      const TimesliceValue = Timeslice[0].value;

      const submitNewtodo = () => {
        const todo = {
          /*id: props.tid,*/
          name: todoName.value,
          priority: Prio,
          category: Cate,
          timeslice: Time,
          done: todoDone,
        };
        context.emit("new-todo", todo);
        //console.log(todoName);

      };
      const getPrio = (name, value, index) => {
        Prio = { name, value };
        console.log("item:", name, value, index);
      };
      const getCate = (name, value, index) => {
        Cate = { name, value };
        console.log("item:", name, value, index);
      };
      const getTime = (name, value, index) => {
        Time = { name, value };
        console.log("item:", name, value, index);
      };

      return {
        submitNewtodo,

        Priority,
        Category,
        Timeslice,
        PriorityValue,
        CategoryValue,
        TimesliceValue,
        todoName,
        getPrio,
        getCate,
        getTime
      };
    },
  };
</script>

<style>
  .newtodo input[class="name"] {
    display: block;
    width: 100%;
    font-size: 20px;
    padding: 16px 24px;
    border-radius: 8px;
    margin-bottom: 24px;
    box-shadow: 0px 0px 24px rgba(230, 230, 250, 0.1);
    background-color: white;
  }

  .newtodo .optionline {
    display: grid;
    grid-template-columns: 120px 120px 120px auto;
    grid-gap: 18px;
    margin-bottom: 24px;
  }


  .newtodo input[type="submit"] {
    appearance: none;
    border: none;
    outline: none;
    display: flex;
    margin-left: auto;
    height: 40px;
    width: 150px;
    font-size: 16px;
    padding: 8px 16px;
    text-align: center;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    font-weight: 700;
    background-color: #AED581;
  }
</style>