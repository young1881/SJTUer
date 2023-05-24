<template>
  <div class="m-select-wrap">
    <input
      :class="['u-select-input', color === 'green' ? 'green-color' : '']"
      type="text"
      readonly
      @click="openSelect"
      @blur="onBlur"
      v-model="selectName"
    />
    <div
      :class="['triangle-down', { rotate: rotate }]"
      @click="openSelect"
    ></div>
    <div
      :class="['m-options-panel', showOptions ? 'show' : 'hidden']"
      :style="`height: ${selectData.length * 40}px;`"
      :appendToBody="true"
    >
      <p
        class="u-option"
        @mousedown="getValue(item.name, item.value, index)"
        v-for="(item, index) in selectData"
        :key="index"
      >
        {{ item.name }}
      </p>
    </div>
  </div>
</template>
<script>
export default {
  name: "SelectData",
  props: {
    selectData: {
      type: Array,
      default: () => {
        return [];
      },
    },
    // eslint-disable-next-line vue/require-prop-types
    selValue: {
      // 将该prop值作为selV的初始值
      default: undefined,
    },
    color: {
      type: String,
      default: () => {
        return "blue";
      },
    },
  },
  computed: {
    selectName() {
      let selName;
      this.selectData.forEach((item) => {
        if (item.value === this.selectValue) {
          selName = item.name;
        }
      });
      return selName;
    },
    selectValue: {
      get() {
        return this.selV;
      },
      set(newVal) {
        this.selV = newVal;
      },
    },
  },
  data() {
    return {
      selV: this.selValue,
      rotate: false,
      showOptions: false,
    };
  },
  methods: {
    openSelect() {
      this.showOptions = !this.showOptions;
      this.rotate = !this.rotate;
    },
    getValue(name, value, index) {
      this.selectValue = value;
      this.$emit("getValue", name, value, index);
    },
    onBlur() {
      this.showOptions = false;
      this.rotate = false;
    },
  },
};
</script>
<style lang="less" scoped>
.m-select-wrap {
  width: 135px;
  height: 40px;
  line-height: 40px;
  position: relative;

  .u-select-input {
    width: 105px;
    background: #3a79ee;
    color: #ffffff;
    box-shadow: 0px 10px 20px 0px rgba(144, 119, 222, 0.2);
    border-radius: 20px;
    height: 40px;
    line-height: 40px;
    padding: 0 15px;
    cursor: pointer;
    border: none;
    font-size: 16px;
  }

  .m-options-panel {
    position: absolute;
    z-index: 10;
  }

  .green-color {
    background: rgb(255, 255, 255, 0.5);
    color: #4f544a;
  }

  .triangle-down {
    // 下三角样式
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 10px solid #111211;
    position: absolute;
    top: 18px;
    right: 40px;
    transition: transform 0.3s ease-in-out;
  }

  .rotate {
    transform: rotate(180deg);
  }

  .m-options-panel {
    position: absolute;
    background: #ffffff;
    border-radius: 8px;
    width: 133px;
    border: 1px solid #e3e3e3;
    top: 46px;
    left: 0;
    color: #404040;
    font-size: 16px;

    .u-option {
      padding: 0 15px;
      cursor: pointer;
    }

    .u-option:hover {
      color: rgb(255, 255, 255, 0.5);
      background: #eef1fa;
    }
  }

  .show {
    display: block;
  }

  .hidden {
    display: none;
  }
}
</style>