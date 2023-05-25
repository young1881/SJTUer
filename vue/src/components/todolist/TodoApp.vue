<template>
  <simple-mode v-if="issimple" :todos="simpleTodos.slice(0, 1)"></simple-mode>
  <div class="container" v-else>
    <div class="todolist">
      <new-todo @new-todo="newTodo" />
      <div class="filter"> 
      <done-filter :selected="filter" @change="filter = $event"></done-filter>
      <option-filter @option-filt="updatefilter"></option-filter>
    </div>
      <todo-list
        class="todo-list"
        @delete-todo="RemoveTodo"
        :todos="Timefilter"
      ></todo-list>
    </div>
  </div>
</template>



<script>
import { ref, onMounted, computed, watch, toRef } from "vue";
import NewTodo from "./NewTodo.vue";
import DoneFilter from "./DoneFilter.vue";
import OptionFilter from "./OptionFilter.vue";
import TodoList from "./TodoList.vue";
//import TodoItem from "./TodoItem.vue";
import SimpleMode from "./SimpleMode.vue";
import axios from "axios";
export default {
  name: "App",
  components: {
    NewTodo,
    DoneFilter,
    OptionFilter,
    TodoList,
    SimpleMode,
  },
  props: {
    simple: Boolean,
  },
  setup(props) {
    const todos = ref([]);

    const issimple = computed(() => {
      return props.simple;
    });
    /*与NewTodo.vue组件相关代码*/
    const newTodo = (todo) => {
      todos.value.push(todo);
      console.log(JSON.stringify(todo));
    };

    /*与DoneFilter.vue组件相关代码*/
    const filter = ref({ lable: "All", value: "all" });
    const filterTodo = computed(() => {
      switch (filter.value) {
        case "done":
          return todos.value.filter((todo) => todo.done);
        case "notdone":
          return todos.value.filter((todo) => !todo.done);
        default:
          return todos.value;
      }
    });
    const donetodo = computed(() => {
      return todos.value.filter((todo) => !todo.done);
    });
    /*与Simpletodo.vue组件相关代码*/
    const simpleTodos = computed(() => {
      const stodo = donetodo;
      stodo.value.sort(function (a, b) {
        return b.priority.value - a.priority.value;
      });
      return stodo.value;
    });

    /*与OptionFilter.vue组件相关代码*/
    let prio = ref("All");
    let cate = ref("All");
    let time = ref("All");
    const updatefilter = (Prio, Cate, Time) => {
      prio.value = Prio;
      cate.value = Cate;
      time.value = Time;
    };
    const Priofilter = computed(() => {
      switch (prio.value) {
        case "All":
          return filterTodo.value;
        default:
          return filterTodo.value.filter(
            (todo) => todo.priority.name === prio.value
          );
      }
    });

    const Catefilter = computed(() => {
      switch (cate.value) {
        case "All":
          return Priofilter.value;
        default:
          return Priofilter.value.filter(
            (todo) => todo.category.name === cate.value
          );
      }
    });

    const Timefilter = computed(() => {
      switch (time.value) {
        case "All":
          return Catefilter.value;
        default:
          return Catefilter.value.filter(
            (todo) => todo.timeslice.name === time.value
          );
      }
    });

    /*与LocalStorage相关代码*/
    const myname = ref("Jiawei");
    watch(myname, (newVal) => {
      localStorage.setItem("myname", newVal);
    });
    watch(
      todos,
      (newVal) => {
        localStorage.setItem("todos", JSON.stringify(newVal));
      },
      {
        deep: true,
      }
    );
    onMounted(() => {
      //myname.value = localStorage.getItem("myname") || "";
      //todos.value = JSON.parse(localStorage.getItem("tasks")) || [];
      todos.value = JSON.parse(localStorage.getItem("todos")) || [];
      todos.value = todos.value.filter((todo) => todo.is_active === true);
      //console.log(JSON.stringify(todos));
    });

    /*与TodoList.vue相关代码*/
    const RemoveTodo = (todo) => {
      todos.value = todos.value.filter((t) => t != todo);

      var params = new URLSearchParams();
      var jaccount = sessionStorage.getItem("jaccount");

      console.log("id:");
      console.log(todo.id);
      params.append("jaccount", jaccount);
      params.append("task_id", todo.id);

      axios
        .post("http://localhost:8000/index/delete_task/", params)
        .then(function (response) {
          // 如果后端删除成功，则返回response.data['key'] = 1；否则返回-1
          console.log("delete task:");
          console.log(response.data["key"]);
        })
        .catch(function (error) {
          // 报错处理
          console.log(error);
        });
    };

    return {
      todos,
      donetodo,
      newTodo,
      filter,
      Timefilter,
      updatefilter,
      RemoveTodo,
      myname,
      simpleTodos,
      issimple,
    };
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Arial;
}

.container {
  width: 80%;
  display: grid;
  text-align: center;
  margin: auto;
  margin-top: 120px;
  border-radius: 20px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.12);
  padding: 50px 30px;
  background-color: rgb(255, 255, 255, 0.5);
}

h1 {
  margin: 24px 0;
  font-size: 30px;
}

input[type="text"],
button {
  appearance: none;
  border: none;
  outline: none;
  background: none;
  cursor: initial;
}
.filter
{
  display: flex;
}

.todo-list {
  max-height: 225px;
  width: 100%;
  overflow-x: auto;
  overflow-y: auto;
}
</style>