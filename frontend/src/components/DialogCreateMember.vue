<template>
  <div class="dialog">
    <div class="dialog__content">
      <div>Добавление участника</div>
      <my-input
        @input-event="inputName"
        :isNecessary="true"
        :inputText="'Напишите имя участника'"
      >
        <template v-slot:title>Участник</template>
      </my-input>

      <my-input @input-event="inputMail" :inputText="'Напишите почту'">
        <template v-slot:title>Почта</template>
      </my-input>

      <my-input @input-event="inputTelNum" :inputText="'Напишите номер'">
        <template v-slot:title> Номер телефона</template>
      </my-input>

      <my-input
        @input-event="inputCountTasks"
        :inputText="'Напишите кол-во задач'"
      >
        <template v-slot:title> Кол-во задач</template>
      </my-input>

      <my-input
        @input-event="inputCountProjects"
        :inputText="'Напишите кол-во проектов'"
      >
        <template v-slot:title> Кол-во проектов</template>
      </my-input>

      <div class="buttons">
        <button-main @clickEvent="sendDataTask">Добавить задачу </button-main>
        <button-text @clickEvent="closeDialog">Отмена</button-text>
      </div>
    </div>
  </div>
</template>

<script>
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "./UI/ButtonMain.vue";
import ButtonText from "./UI/ButtonText.vue";

export default {
  emits: ["input-event", "click-event"],
  data() {
    return {
      name: "",
      mail: "",
      telNum: "",
      countTasks: 0,
      countProjects: 0,
    };
  },
  components: {
    MyInput,
    ButtonMain,
    ButtonText,
  },
  methods: {
    sendDataTask() {
      const html = document.querySelector("html");
      html.classList.remove("lock");
      this.$emit("close-dialog", {
        name: this.name,
        mail: this.mail,
        telNum: this.telNum,
        countTasks: this.countTasks,
        countProjects: this.countProjects,
        rating: 1
      });
    },
    inputName(name) {
      this.name = name;
    },
    inputMail(mail) {
      this.mail = mail;
    },
    inputTelNum(telNum) {
      this.telNum = telNum;
    },
    inputCountTasks(countTasks) {
      this.countTasks = countTasks;
    },
    inputCountProjects(countProjects) {
      this.countProjects = countProjects;
    },

    closeDialog() {
      const html = document.querySelector("html");
      html.classList.remove("lock");
      this.$emit("close-dialog", {});
    },
  },

  mounted() {
    const html = document.querySelector("html");
    html.className = "lock";
  },
};
</script>

<style  lang="scss" scoped >
.dialog {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  backdrop-filter: blur(2px);
  p {
    margin: 0;
  }
  .dialog__content {
    width: 30%;
    border-radius: 16px;
    // height: 40%;
    padding: 3%;
    background: var(--base-02);
    .roles {
      display: flex;
      flex-wrap: wrap;
      .role {
        margin: 0 2% 2% 0;
        padding: 2% 2%;
        border-radius: 12px;
        border: var(--Input-stroke-hover) solid 1px;
        display: flex;
        align-items: center;
        p {
          margin: 0;
        }
      }
    }
    .buttons {
      display: flex;
      margin: 3% 0;
    }
  }
}
</style>