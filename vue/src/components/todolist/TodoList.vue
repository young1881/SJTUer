<template>
  <div class="todolist" v-if="todos">
    <todo-item v-for="todo in todos" :key="todo.name" :listItem="todo" @statuschange="doneChange(todo)"
      @item-deleted="deleteToDo(todo)"></todo-item>
  </div>
</template>

<script>
import TodoItem from "./TodoItem.vue";
import axios from "axios";
export default {
  name: "TodoList",
  components: { TodoItem },
  props: ["todos"],
  setup(props,context){
    const deleteToDo = (todo) => {
      context.emit("delete-todo",todo);
      //console.log(todo.name);
    }
    const doneChange = (todo) =>{
      todo.done = !todo.done;
      var params = new URLSearchParams()
      var jaccount = sessionStorage.getItem("jaccount");

      console.log(todo.id)
      params.append('jaccount', jaccount);
      params.append('task_id', todo.id);
      params.append('task_done', todo.done);

      axios
      .post('http://localhost:8000/index/done_task/',params)
      .then(function(response){
        // 如果后端添加成功，则返回response.data['key'] = 1；否则返回-1
        console.log("Done task:")
        console.log(response.data['key'])
        
      })
      .catch(function(error){
        // 报错处理
        console.log(error)
      })
    };
    return{
      deleteToDo,
      doneChange,
    };
  },
  
};
</script>

<style>
  .todolist {
    display: grid;
    row-gap: 14px;
  }
</style>