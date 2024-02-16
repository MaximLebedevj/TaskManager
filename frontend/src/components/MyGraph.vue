

<template>
  <div @click.self.prevent="createTask" class="graph">
    <my-task
      :x="task[0]"
      :y="task[1]"
      :key="task"
      v-for="task in taskСoordinates"
    />
  </div>
</template>

<script >
import MyTask from "./MyTask.vue";

export default {
  components: {
    MyTask,
  },
  data() {
    return {
      taskСoordinates: [],
    };
  },
  methods: {
    createTask(e) {
      const graph = document.querySelector(".graph");
      let x = e.pageX - graph.offsetLeft;
      let y = e.pageY - graph.offsetTop;

      this.taskСoordinates.push([x, y]);
    },
  },
};
</script>

<style lang="scss" scoped>
.graph {
  position: relative;
  height: 100vh;
  width: 100%;
  border: 1px red solid;
  z-index: 0;
}
</style>