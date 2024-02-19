<template>
  <div class="dialog">
    <div class="dialog__content">
      <my-input @input-event='inputName' :isNecessary="true" :inputText="'Напишите название'">
        <template v-slot:title> Название</template>
      </my-input>
      <my-input @input-event='inputDescription' :isNecessary="false" :inputText="'Напишите описание'">
        <template v-slot:title> Описание</template>
      </my-input>
      <p>Роль</p>
      <div class="roles">
        <div class="role" :key="role.name" v-for="role in roles">
          <p>{{ role.name }}</p>
          <img
            @click="deleteRole(role.name)"
            src="../assets/icons/Type=Cross, State=Default.svg"
            alt=""
          />
        </div>
      </div>
      <p v-if="!openInputAddRole" @click="openInputAddRole = true">
        Добавить роль
      </p>
      <my-input
        v-if="openInputAddRole"
        @input-enter-event="createRole"
        :isNecessary="false"
        :inputText="'Напишите название роли'"
      ></my-input>
      <div class="buttons">
        <button-main @clickEvent="clickEvent"
          >Добавить организацию
        </button-main>
        <button-text @clickEvent="clickEvent">Отмена</button-text>
      </div>
    </div>

  </div>

</template>

<script>
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "./UI/ButtonMain.vue";
import ButtonText from "./UI/ButtonText.vue";

export default {
     emits: ['input-event', 'click-event'],
    data() {
        return {
            roles:[
                {name: "Веб-дизайнер"},
                {name: "Frontend-разработчик"},
                {name: "Backend-разработчик"},
                {name: "Продакт менеджер"},
            ],
            nameOrganization: '',
            descriptionOrganization: "",
            openInputAddRole: false
        }
    },
    components: {
        MyInput,ButtonMain, ButtonText
    },
    methods: {
        deleteRole(roleName) {
            this.roles = this.roles.filter(role => role.name !== roleName);
        },
        createRole(name) {
            this.roles.push({name: name})
            this.openInputAddRole = false
        },
          addOrganization() {
            this.$emit('input-event', this.inputValue)
        },
        clickEvent() {
            this.addOrganization() 
            this.$emit('close-dialog', {
              'roles': this.roles,
              'name': this.nameOrganization,
              'description':  this.descriptionOrganization,
              'countTasks': 0,
              'countMembers': 0

            })
        },
        inputName(name) {
          this.nameOrganization = name
        },
        inputDescription(description) {
          this.descriptionOrganization = description
        }

    },

    mounted() {
        const html = document.querySelector('html')
        html.className = 'lock'
    }
}
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
  // opacity: 0.6;
  backdrop-filter: blur(2px);
  p {
    margin: 0;
  }
  .dialog__content {
    width: 30%;
    border-radius: 16px;
    // height: 40%;
    padding: 0 3%;
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