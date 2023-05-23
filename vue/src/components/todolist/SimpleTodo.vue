<template>
  <div class="incard">
    <label>
      <input type="checkbox" :checked="listItem.done" @click="$emit('statuschange', listItem)" />
      {{ listItem.name }}
      <span class="bubble"></span>
    </label>
  </div>
</template>

<script>
  export default {
    name: "SimpleTodo",
    props: ["listItem"],
  };
</script>

<style>
  .incard {
    display: flex;
    align-items: center;
    padding: 1px;
    border-radius: 8px;
    min-width: 200px;
  }

  .incard label {
    display: flex;
    position: relative;
    cursor: pointer;
    width: 100%;
    padding: 10px;
    text-align: center;
    overflow: hidden;
    text-align: left;
    font-size: 20px;

    /*
  display: flex;
  position: relative;
  align-content: center;
  cursor: pointer;
  width: 70%;
  */
  }

  .incard label span.bubble {
    position: absolute;
    top: 0;
  }

  .incard label span.bubble::before,
  .incard label span.bubble::after {
    content: "";
    display: block;
    position: absolute;
    width: 18px;
    height: 18px;
    border-radius: 50%;
  }

  .incard label span.bubble::before {
    border: 1px solid #9ccc65;
  }

  .incard label span.bubble::after {
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
    margin-left: 30px;
    opacity: 0;
  }

  .incard input:checked+span.bubble::after {
    width: 10px;
    height: 10px;
    opacity: 1;
  }
</style>