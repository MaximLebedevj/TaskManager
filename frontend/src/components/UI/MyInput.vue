<template>
  <p  class="title"><slot name="title"> </slot>
  <span class="necessary" v-if="isNecessary"> *</span>
  </p>

  <input @keydown.enter='inputEvent' v-model="inputValue" class="input" type="text" :placeholder="inputText" />
</template>

<script>
export default {
  props: {
    inputText: String,
    isNecessary: Boolean
  },
  data(){
      return {
          inputValue: ''
      }
  },
  methods: {
      inputEvent() {
          this.$emit('input-event', this.inputValue)
      }
  }
};
</script>

<style lang="scss">
.title {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 122%;

  color: var(--text-01);
}
.input {
    width: 100%;
    border-radius: 8px;
    padding: 14px 16px;
    border: #D9D9D9 solid 1px;
}
.necessary {
    color:red;
}
</style>