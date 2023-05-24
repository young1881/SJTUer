<template>
  <div class="contain">
    <div class="simplebox">
      <div class="card">
        <p>Your Todos</p>
        <div v-if="todos.length">
          <simple-todo
            v-for="todo in todos"
            :key="todo.name"
            :listItem="todo"
            @statuschange="doneChange(todo)"
          ></simple-todo>
        </div>
        <div class="finish" v-else>
          <h2>Congrats! You've finished all tasks</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SimpleTodo from "./SimpleTodo.vue";
import axios from "axios";
export default {
  name: "SimpleMode",
  components: { SimpleTodo },
  props: ["todos"],
  setup() {
    const doneChange = (todo) => {
      todo.done = !todo.done;
      var params = new URLSearchParams();
      var jaccount = sessionStorage.getItem("jaccount");

      console.log(todo.id);
      params.append("jaccount", jaccount);
      params.append("task_id", todo.id);
      params.append("task_done", todo.done);

      axios
        .post("http://localhost:8000/index/done_task/", params)
        .then(function (response) {
          // 如果后端添加成功，则返回response.data['key'] = 1；否则返回-1
          console.log("Done task:");
          console.log(response.data["key"]);
        })
        .catch(function (error) {
          // 报错处理
          console.log(error);
        });
    };
    return {
      doneChange,
    };
  },
};
</script>

<style>
.contain {
  display: grid;
  justify-content: center;
  align-items: center;
  margin: auto;
  margin-top: 150px;
  background: none;
}

.simplebox {
  display: flex;
  text-align: center;
  margin-top: 10%;
}

.card {
  background-color: var(--background);
  display: block;
  width: 380px;
  min-height: 120px;
  cursor: pointer;
  padding: 15px;
  margin: 0px;
  border: 3px solid var(--primary);
  box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--green),
    20px -20px 0 -3px var(--background), 20px -20px var(--yellow),
    30px -30px 0 -3px var(--background), 30px -30px var(--orange),
    40px -40px 0 -3px var(--background), 40px -40px var(--red);
}

.card:hover {
  animation: shadow-wave 1.5s ease infinite;
}

@keyframes shadow-wave {
  0% {
    border: 3px solid var(--primary);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--green),
      20px -20px 0 -3px var(--background), 20px -20px var(--yellow),
      30px -30px 0 -3px var(--background), 30px -30px var(--orange),
      40px -40px 0 -3px var(--background), 40px -40px var(--red);
  }

  20% {
    border: 3px solid var(--red);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--primary),
      20px -20px 0 -3px var(--background), 20px -20px var(--green),
      30px -30px 0 -3px var(--background), 30px -30px var(--yellow),
      40px -40px 0 -3px var(--background), 40px -40px var(--orange);
  }

  40% {
    border: 3px solid var(--orange);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--red),
      20px -20px 0 -3px var(--background), 20px -20px var(--primary),
      30px -30px 0 -3px var(--background), 30px -30px var(--green),
      40px -40px 0 -3px var(--background), 40px -40px var(--yellow);
  }

  60% {
    border: 3px solid var(--yellow);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--orange),
      20px -20px 0 -3px var(--background), 20px -20px var(--red),
      30px -30px 0 -3px var(--background), 30px -30px var(--primary),
      40px -40px 0 -3px var(--background), 40px -40px var(--green);
  }

  80% {
    border: 3px solid var(--green);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--yellow),
      20px -20px 0 -3px var(--background), 20px -20px var(--orange),
      30px -30px 0 -3px var(--background), 30px -30px var(--red),
      40px -40px 0 -3px var(--background), 40px -40px var(--primary);
  }

  100% {
    border: 3px solid var(--primary);
    box-shadow: 10px -10px 0 -3px var(--background), 10px -10px var(--green),
      20px -20px 0 -3px var(--background), 20px -20px var(--yellow),
      30px -30px 0 -3px var(--background), 30px -30px var(--orange),
      40px -40px 0 -3px var(--background), 40px -40px var(--red);
  }
}

:root {
  --primary: #22d2a0;
  --secondary: #192824;
  --background: rgba(255, 255, 255, 0.5);
  --green: #1fc11b;
  --yellow: #ffd913;
  --orange: #ff9c55;
  --red: #ff5555;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  background-image: radial-gradient(
    var(--secondary) 30%,
    var(--background) 30%
  );
  background-size: 2px 3px;
  font-family: "Archivo", sans-serif;
  color: var(--primary);
}

.card p {
  font-size: 20px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 5px;
  margin-top: 15px;
  font-weight: bold;
}

.finish {
  display: grid;
  margin-top: 15px;
}

h2 {
  font-size: 20px;
  font-family: "Archivo Black", "Archivo", sans-serif;
  font-weight: bold;
}
</style>