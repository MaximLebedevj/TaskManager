<template>
  <div
    :style="{
      left: x - widthTask + 'px',
      top: y - heightTask + 'px',
      'min-width': widthTask * 2 + 'px',
      'min-height': heightTask * 2 + 'px',
    }"
    class="wrapper__task"
  >
    <div
      :style="{
        width: widthTask + 'px',
        height: heightTask + 'px',
      }"
      class="task"
    >
      {{ selectPlaceArrow }}
      <button @click="createArrow" class="task__arrow task__arrow_top"></button>
      <button
        @mousedown="createArrow"
        class="task__arrow task__arrow_right"
      ></button>
      <button
        @mousedown="createArrow"
        class="task__arrow task__arrow_bottom"
      ></button>
      <button
        @mousedown="createArrow"
        class="task__arrow task__arrow_left"
      ></button>
    </div>
  </div>
</template>

<script setup >
defineProps({
  x: Number,
  y: Number,
});
import { ref } from "vue";
const widthTask = ref(140);
const heightTask = ref(50);

const arrows = []; // [start, end]

const graph = document.querySelector(".graph");
let selectPlaceArrow = ref(false);
function createArrow(e) {
  let startX = e.clientX - graph.offsetLeft;
  let startY = e.clientY - graph.offsetTop;
  let endX = e.clientX - graph.offsetLeft;
  let endY = e.clientY - graph.offsetTop;

  let selectPlaceArrow = ref(true);

  function onMouseMove(e) {
    console.log(endX, endY);
  }

  document.addEventListener("mousemove", onMouseMove);

  // removeEventListener
  document.addEventListener(
    "mouseup",
    () => (selectPlaceArrow = ref(false)),
    document.removeEventListener("mousemove", onMouseMove)
  );
}
</script>
<style lang="scss" scoped>
$sizeArrow: 16;

.wrapper__task {
  position: absolute;

  //   border: 1px black solid;
  display: flex;
  align-items: center;
  justify-content: center;
  .task {
    position: relative;
    border: 1px green solid;
    z-index: 1;
    .task__arrow {
      position: absolute;
      width: $sizeArrow + px;
      height: $sizeArrow + px;
      border-radius: 50%;
      background: grey;
      border: none;
      padding: 0;
    }
    .task__arrow_top {
      top: calc(-1 * $sizeArrow / 2) + px;
      left: 50% - calc($sizeArrow / 3);
    }
    .task__arrow_right {
      top: 50% - $sizeArrow;
      right: calc(-1 * $sizeArrow / 2) + px;
    }
    .task__arrow_bottom {
      bottom: calc(-1 * $sizeArrow / 2) + px;
      left: 50% - calc($sizeArrow / 3);
    }
    .task__arrow_left {
      top: 50% - $sizeArrow;
      left: calc(-1 * $sizeArrow / 2) + px;
    }
  }
}
</style>