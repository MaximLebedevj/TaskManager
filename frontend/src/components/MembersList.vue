<template>
<div>
    <div class="additionally" >
        <div class="button" >
            <button-main @click-event="isOpenDialogCreatMember=true">Добавить участника</button-main>
        </div>
    </div>
<div class="members-list" >

    <div class="membersList__item" v-for="member in members" :key="member.name">
        <div class="item__text">{{member.name}}</div>
        <div class="item__text">{{member.email}}</div>
        <div class="item__text">{{member.telNum}}</div>
        <div class="item__text">{{member.countTask}}</div>
        <div class="item__text">{{member.countProjects}}</div>
        <div class="item__text">{{member.rating}}</div>

    </div>
</div>
    <dialog-create-member @close-dialog='closeDialog' v-if="isOpenDialogCreatMember"> </dialog-create-member>


</div>

</template>

<script>
import ButtonText from "../components/UI/ButtonText.vue";
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "../components/UI/ButtonMain.vue";
import DialogCreateMember from "../components/DialogCreateMember.vue";

export default {
    emits: ["input-event"],
  components: {
    MyInput,
    ButtonMain,
    ButtonText,
    ButtonText,
    DialogCreateMember
  },
  props: {
      members: Array
  },
  data() {
    return {
        isOpenDialogCreatMember: false
    };
  },
  methods: {
    closeDialog(newMembers) {
      const html = document.querySelector("html");
      html.classList.remove("lock");
      if (Object.keys(newMembers  ).length != 0) {
          this.members.push(newMembers)
        //   this.$store.commit('pushOrganization', newOrganization)

      }
      this.isOpenDialogCreatMember = false;
    },


  },

  computed: {

  },
  
};
</script>

<style lang="scss" scoped>
.additionally {
    display: flex;
    justify-content: flex-end;
    .button {
        width: 15%;
    }
}

.members-list {
    display: flex;
    flex-direction: column;
    .membersList__item {
        padding: 2%;
        background: var(--base-02);
        border-radius: 8px;
        margin: 1% 0 0 0;
        height: 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        top: 0;
        left: 0;
        .item__text{
            position:  absolute;
        }
        .item__text:nth-child(2){
            position:  absolute;
            left: 17%;
        }
        .item__text:nth-child(3){
            position:  absolute;
            left: 34%;
        }
        .item__text:nth-child(4){
            position:  absolute;
            left: 50%;
        }
        .item__text:nth-child(5){
            position:  absolute;
            left: 70%;
        }
        .item__text:nth-child(6){
            position:  absolute;
            left: 95%;
        }
    }
}
</style>