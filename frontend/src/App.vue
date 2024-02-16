<script setup>
import MyHeader from "./components/MyHeader.vue";
import MyGraph from "./components/MyGraph.vue";
</script>

<template>
  <my-header />
  <router-view></router-view>
  <!-- <my-graph /> -->
</template>


  
<style lang="scss"  >
html,
body {
  margin: 0;
  padding: 0;
}
body {
  background: #f7f7f7;
}
*,
a:focus {
  outline: none !important;
}

* {
  box-sizing: border-box;
}
</style>
