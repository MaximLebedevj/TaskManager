<template>
  <div class="wrapper">
    <div class="info">
      <h2 class="info__title">ОРГАНИЗАЦИИ </h2>
      <div class="info__btn_wrapper">
        <button-main :isDisabled="!$store.state.isAuthorized" @click-event="openDialog">
          Добавить организацию</button-main
        >
      </div>
    </div>
    <div class="organizations" v-if="$store.state.isAuthorized">
      <div class="organizations__items">
        <div
          class="organizations__item"
          :key="organization.name"
          v-for="organization in $store.state.organizations"
          @click="$router.push(`Organizations/ ${organization.name}`)"
        >
          <div class="item__imgWrapper">
            <img
              class="item__img"
              src="../assets/organizationCard.png"
              alt=""
            />
          </div>
          <h3 class="item__title">{{ organization.name }}</h3>
          <div class="item__info">
            <p class="info__text">Кол-во задач {{ organization.countTasks }}</p>
            <p class="info__text">
              Кол-во участников {{ organization.countMembers }}
            </p>
          </div>
        </div>
      </div>
    </div>
  
    <div v-else class="organizations_notAuth">
      <div class="organizations__content">
        <img class="content__img" src="../assets/notAuth.png" alt="" />
        <p class="content-text1">Вы не вошли в аккаунт</p>
        <p class="content-text2">
          Авторизируйетсь или создайте новый аккаунт, чтобы создать новый
          организацию или посмотреть старые
        </p>
        <div class="content__button">
          <ButtonMain  @click-event='$router.push("registration")' > Зарегистрироваться</ButtonMain>
        </div>
        <div class="content__haveAccount">
          <p>Уже есть аккаунт?</p>
          <button-text> Войти</button-text>
        </div>
      </div>

    </div>
              <dialog-create-organization
      @close-dialog="closeDialog"
      v-if="isOpenDialog"
    />
  </div>

</template>

<script >
import DialogCreateOrganization from "../components/DialogCreateOrganization.vue";
import ButtonText from "../components/UI/ButtonText.vue";
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "../components/UI/ButtonMain.vue";
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'
export default {
  emits: ["input-event", "close-dialog"],
  components: {
    DialogCreateOrganization,
    MyInput,
    ButtonMain,
    ButtonText,
    ButtonText,
  },
  
  data() {
    return {
      organizations: [
        { name: "Название 1", countTasks: 0, countMembers: 0 },
        { name: "Название 2", countTasks: 1, countMembers: 1 },
        { name: "Название 2", countTasks: 1, countMembers: 1 },
      ],
      isOpenDialog: false,
    };
  },
  methods: {
    closeDialog(newOrganization) {
      const html = document.querySelector("html");
      html.classList.remove("lock");
      if (Object.keys(newOrganization  ).length != 0) {
          this.$store.commit('pushOrganization', newOrganization)

      }
      this.isOpenDialog = false;
    },
    openDialog() {
      this.isOpenDialog = true
    }
  },
  computed: {},
};
</script>

<style lang="scss">
.wrapper {
  height: auto;
  padding: 0 5%;
}
.info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  .info__title {
    font-weight: 500;
    font-size: 24px;
  }
  .info__btn_wrapper {
    width: 100%;
    max-width: 13% !important;
  }
}
.organizations {
  position: relative;
  height: 100%;

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
.organizations_notAuth {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  // flex-direction: column;
  text-align: center;
  .organizations__content {
    max-width: 469px;
    display: flex;
    // justify-content: center;
    flex-direction: column;
    align-items: center;
    .content-text1 {
      font-family: "Inter";
      font-style: normal;
      font-weight: 400;
      font-size: 18px;
      line-height: 132%;
      color: var(--text-01);
      margin: 0;
    }
    .content-text2 {
      font-family: "Inter";
      font-style: normal;
      font-weight: 400;
      font-size: 16px;
      line-height: 122%;

      color: var(--text-02);
    }
    .content__button {
      width: 80%;
    }
    .content__haveAccount {
      display: flex;
      p {
        white-space: nowrap;
      }
    }
  }
}
</style>