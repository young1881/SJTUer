<template>
  <div class="statusfilter">
    <span
      v-for="filter in filters"
      :key="filter.value"
      class="filter"
      :class="{ active: selected === filter.value }"
      @click="$emit('change', filter.value)"
      >{{ filter.label }}</span
    >
  </div>
</template>

<script>
export default {
  name: "DoneFilter",
  props: ["selected"],
  setup() {
    const filters = [
      { label: "All", value: "all" },
      { label: "Done", value: "done" },
      { label: "Not Done", value: "notdone" },
    ];
    return {
      filters,
    };
  },
};
</script>

<style>
.statusfilter {
  display: flex;
  margin: 24px, 2px;
  color: #c0c2ce;
  font-size: 18px;
  margin-left: 8px;
  margin-bottom: 0px;
}

.statusfilter .filter {
  margin-left: 14px;
  transition: 0.4s;
}

.statusfilter .filter:hover {
  cursor: pointer;
}

.statusfilter .filter.active {
  color: #6b729c;
}
</style>