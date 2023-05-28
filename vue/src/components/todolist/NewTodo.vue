<template>
  <div class="newtodo">
    <div class="regular" :class="{ active: massageFlag === true }" >
      <input
        type="text"
        class="name"
        v-model="todoName"
        placeholder="e.g Homework"
      />
      <div class="optionline">
        <!--
      <input type="text" class="option" placeholder="priority" />
      <input type="text" class="option" placeholder="category" />
      <input type="text" class="option" placeholder="timeslice" />
      !-->
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
        <input type="submit" value="Add Todo" @click="submitNewtodo" />
      </div>
    </div>
    <div class="massagebox" v-if="massageFlag">
      {{ noPermission }}
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import SelectData from "./SelectData.vue";
import axios from "axios";
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
    const todoDone = ref < Boolean > "False";
    let Prio = { name: "Low", value: 1 };
    let Cate = { name: "School", value: 1 };
    let Time = { name: "5min", value: 1 };
    const PriorityValue = Priority[0].value;
    const CategoryValue = Category[0].value;
    const TimesliceValue = Timeslice[0].value;
    let massageFlag = ref(false);
    let noPermission = ref("");

    const submitNewtodo = () => {
      const todo = {
        id: -1,
        name: todoName.value,
        category: Cate,
        done: todoDone,
        priority: Prio,
        timeslice: Time,
        is_active: true,
      };
      if (todoName.value == "") {
        showMessage("输入不能为空！");
        return;
      }
      //context.emit("new-todo", todo);
      //console.log(todoName);
      var params = new URLSearchParams();
      var jaccount = sessionStorage.getItem("jaccount");

      params.append("jaccount", jaccount);
      params.append("name", todoName.value);
      params.append("priority", Prio["value"]);
      params.append("category", Cate["value"]);
      params.append("timeslice", Time["value"]);
      params.append("done", todoDone);

      axios
        .post("http://localhost:8000/index/add_task/", params)
        .then(function (response) {
          console.log("add task:");
          console.log(response.data["key"]);
          // 如果后端添加成功，则返回response.data['key'] = id；否则返回-1
          // 把id添加到todo结构体中
          if (response.data["key"] != -1) {
            todo.id = response.data["key"];
          }
          context.emit("new-todo", todo);
        })
        .catch(function (error) {
          // 报错处理
          console.log(error);
        });
        
        todoName.value = "";
    };

    const showMessage = (text) => {
      noPermission.value = text;
      massageFlag.value = true;
      setTimeout(() => {
        massageFlag.value = false;
      }, 666);
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
      massageFlag,
      noPermission,
      submitNewtodo,
      showMessage,
      Priority,
      Category,
      Timeslice,
      PriorityValue,
      CategoryValue,
      TimesliceValue,
      todoName,
      getPrio,
      getCate,
      getTime,
    };
  },
};
</script>

<style>
.newtodo input[class="name"] {
  display: flex;
  width: 100%;
  height: 42px;
  font-size: 20px;
  padding: 8px 24px;
  border-radius: 8px;
  margin-bottom: 16px;
  box-shadow: 0px 0px 24px rgba(230, 230, 250, 0.1);
  background-color: white;
}

.newtodo .optionline {
  display: grid;
  grid-template-columns: 96px 96px 96px auto;
  grid-gap: 18px;
  margin-left: 4px;
  margin-bottom: 4px;
}

.newtodo input[type="submit"] {
  appearance: none;
  border: none;
  outline: none;
  display: flex;
  margin-left: auto;
  height: 35px;
  width: 100px;
  font-size: 14px;
  padding: 8px 16px;
  text-align: center;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  font-weight: 700;
  background-color: #aed581;
  margin-bottom: 0px;
}
.newtodo input[type="submit"]:hover {
  cursor: pointer;
  opacity: 0.75;
}
.regular.active{
  opacity: 0.5;
}
</style>