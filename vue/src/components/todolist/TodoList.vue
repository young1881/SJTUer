<template>
  <div class="todolist"  v-if ="todos">
    <todo-item
      v-for="todo in todos"
      :key="todo.name"
      :listItem= "todo"
      @statuschange="todo.done = $event.target.checked"
      @item-deleted="deleteToDo(todo)"
    ></todo-item>
  </div>
</template>

<script>
import TodoItem from "./TodoItem.vue";
export default {
  name: "TodoList",
  components: { TodoItem },
  props: ["todos"],
  setup(props,context){
    const deleteToDo = (todo) => {
      context.emit("delete-todo",todo);
      //console.log(todo.name);
    };
    return{
      deleteToDo,
    };
  }
};
</script>

<style>
.todolist {
  display: grid;
  row-gap: 14px;
}
</style>