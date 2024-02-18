<template>
  <div>
      <div class="organizations">
    <div class="organizations__info" >
      <h2 class="organizations__title">ОРГАНИЗАЦИИ {{}}</h2>
      <button class="organizations__btn" @click="isOpenDialog = true">Добавить организацию</button>

    </div>
    <div class="organizations__items" >

      <div class="organizations__item" :key="organization.title" v-for="organization in organizations" >
        <div class="item__imgWrapper">
          <img class="item__img" src="../assets/organizationCard.png" alt="" />
        </div>
        <h3 class="item__title">{{organization.title}}</h3>
        <div class="item__info">
          <p class="info__text">Кол-во задач {{organization.countTasks}}</p>
          <p class="info__text">Кол-во участников {{organization.countMembers}}</p>
        </div>
      </div>
    </div>
  </div>
  <dialog-create-organization @close-dialog='closeDialog' v-if="isOpenDialog" /> 
  </div>


</template>

<script >
import DialogCreateOrganization from "../components/DialogCreateOrganization.vue";


export default {
  emits: ['input-event', 'close-dialog'],
    components: {
    DialogCreateOrganization,
  },
     
  data() {
    return {
      organizations: [
        { title: "Название 1", countTasks: 0, countMembers: 0 },
        { title: "Название 2", countTasks: 1, countMembers: 1 },
        { title: "Название 2", countTasks: 1, countMembers: 1 },

      ],
      isOpenDialog: false
    };
  },
  methods: {
    closeDialog(){
      const html = document.querySelector('html')
      html.classList.remove('lock')
      this.isOpenDialog = false
    }
  },
  computed: {},
};
</script>

<style lang="scss">
.organizations {
  position: relative;
  padding: 0 5%;
  height: 100%;
  .organizations__info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    .organizations__title {
      font-weight: 500;
      font-size: 24px;
    }
    .organizations__btn {
      color: var(--text-01);
      padding: 14px 24px;
      background: var(--action-default);
      border-radius: 8px;
      height: 100%;
      /* Создать проект */


        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 16px;
        line-height: 19px;

        color: var(--black-button-text);


    }
  }

  .organizations__items {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(345px, 1fr));
    gap: 20px;
    .organizations__item {
      width: 100%;
      .item__imgWrapper {
        background: var(--base-02);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .item__title {
        padding: 0 16px;
        margin: 0;
        font-weight: 500;
        font-size: 24px;
      }
      .item__info {
        padding: 0 16px;

        display: flex;
        justify-content: space-between;
        .info__text {
          color: var(--text-02);
        }
      }
    }
  }
  

}
</style>