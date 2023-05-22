<template>
  <div class="todoitem" v-if="listItem">
    <label>
      <input
        type="checkbox"
        :checked="listItem.done"
        @click="$emit('statuschange', $event)"
      />
      {{ listItem.name }}
      <span class="bubble"></span>
    </label>

    <span class="prio">{{ listItem.priority.name }}</span>
    <span class="prio">{{ listItem.category.name }}</span>
    <span class="prio">{{ listItem.timeslice.name }}</span>
    <div class="delete">
      <button @click="deleteToDo">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["listItem"],
  setup(props, context) {
    const deleteToDo = () => {
      context.emit("item-deleted");
      //console.log(1)
    };

    return {
      deleteToDo,
    };
  },
};
</script>

<style>
.todolist .todoitem {
  display: flex;
  align-items: center;
  background-color: white;
  padding: 8px;
  border-radius: 8px;
  color: #414837;
}

.todoitem label {
  display: flex;
  position: relative;
  align-content: center;
  cursor: pointer;
  width: 70%;

  padding: 10px;
  font: 20px;
  text-align: center;
  overflow: hidden;
  
  /*
  display: flex;
  position: relative;
  align-content: center;
  cursor: pointer;
  width: 70%;
  */
}

.todoitem label span.bubble {
  position: absolute;
  top: 0;
}
.todoitem label span.bubble::before,
.todoitem label span.bubble::after {
  content: "";
  display: block;
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 50%;
}

.todoitem label span.bubble::before {
  border: 1px solid #9ccc65;
}

.todoitem label span.bubble::after {
  content: "";
  display: block;
  opacity: 0;
  width: 0px;
  height: 0px;
  background-color: #9ccc65;
  border-radius: 50%;
  transition: 0.2s ease-in-out;
  box-shadow: 0px 0px 24px rgba(156, 204, 101, 0.1);
}
input[type="checkbox"] {
  display: flex;
  margin-left: 22px;
  opacity: 0;
}

.todoitem input:checked + span.bubble::after {
  width: 10px;
  height: 10px;
  opacity: 1;
}

.todoitem .prio {
  display: block;
  padding: 8px;
  width: 70px;
  background: #b39ddb;
  justify-items: center;
  align-items: center;
  text-align: center;
  border-radius: 16px;
  color: white;
  margin-left: 12px;
}

.todoitem .delete {
  display: block;
  padding: 8px;
  border-radius: 5px;
  margin-left: 50px;
}
.todoitem .delete button:hover {
  opacity: 0.75;
}
.bubble {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid;
}
.todoitem .delete {
  display: flex;
  height: 40px;
  width: 100px;
  flex-direction: column;
  text-align: center;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  padding: 8px 16px;
  border-radius: 24px;
  font-weight: 700;
  background-color: #dcedc8;
}
.todoitem .delete:hover{
  background-color: #ceeaae;
  cursor: pointer;
}
</style>