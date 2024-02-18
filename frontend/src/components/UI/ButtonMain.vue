<template>
    <button @click="clickEvent" >
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
display: flex;
justify-content: center;
align-items: center;
padding: 10px 0;


background: var(--action-default);
border-radius: 8px;
color: var(--black-button-text);

/* Создать проект */

font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 19px;




}
button:hover {
    background: var(--action-hover);
}
</style>