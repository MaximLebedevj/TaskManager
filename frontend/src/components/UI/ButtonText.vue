<template>
    <button  @click="clickEvent">
        <slot> </slot>
    </button>
</template>
<script>
export default {
    methods: {
    clickEvent() {
          this.$emit('clickEvent')
      }
    }
}
</script>

<style lang="scss" scoped>
button {
    width: 100%;
    background: none;
    /* Личный кабинет */
    border: none;

/* Main text */
font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 122%;


color: var(--action-default);
cursor: pointer;

}
</style>