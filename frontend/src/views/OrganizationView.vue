<template>
  <div class="organization">
    <p>Организация</p>
    <h2>{{ $route.params.nameOrganization }}</h2>
    <div class="organization__nav" >
      <a class="nav__item" :class="{'select': isOpenProjects}" @click="isOpenProjects = true, isOpenDescription = false, isOpenMembers = false " >
      <p>Проекты</p>
       <span class="underline" v-if="isOpenProjects"></span>
       </a>
      <a class="nav__item" :class="{'select': isOpenDescription}" @click="isOpenDescription = true, isOpenProjects = false, isOpenMembers = false" >
      <p>Описание</p>
       <span class="underline" v-if="isOpenDescription"></span>
       </a>
      <a class="nav__item" :class="{'select': isOpenMembers}" @click="isOpenMembers = true, isOpenProjects = false, isOpenDescription = false" >
      <p>Участники</p>
       <span class="underline" v-if="isOpenMembers"></span>
       </a>

    </div>

    <tasks-list v-if="isOpenProjects" :tasks='organization.tasks'> </tasks-list>
    <organization-description v-else-if="isOpenDescription" >{{organization.description}}</organization-description>
    <members-list :members='organization.members' v-else> </members-list>
  </div>
</template>

<script>
import DialogCreateTask from "../components/DialogCreateTask.vue";
import ButtonText from "../components/UI/ButtonText.vue";
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "../components/UI/ButtonMain.vue";
import TasksList from "../components/TasksList.vue";
import OrganizationDescription from "../components/OrganizationDescription.vue";
import MembersList from "../components/MembersList.vue";


export default {
    emits: ["input-event", "close-dialog"],
  components: {
    DialogCreateTask,
    MyInput,
    ButtonMain,
    ButtonText,
    ButtonText,
    TasksList,
    OrganizationDescription,
    MembersList
  },
  data() {
    return {
      organization:  this.$store.getters.getTasksByName(this.$route.params.nameOrganization.slice(1)),
      isOpenDialog: false,

      isOpenProjects: true,
      isOpenDescription: false,
      isOpenMembers: false
    };
  },
  methods: {
      createNewTask(newTask) {
      if (Object.keys(newTask  ).length != 0) {
          this.tasks.push(newTask);
      }
        this.isOpenDialog = false
      },
      // getTasksByName() {
      //   const organization = this.$store.getters.getTasksByName(this.$route.params.nameOrganization.slice(1))
      //   this.organization = organization
      // }
  },
  mounted() {
  //  this.getTasksByName()

  },
  computed: {

  }
};
</script>

<style lang="scss" scoped>
.organization {
  padding: 0 5%;
  .organization__nav {
    display: flex;
    .nav__item {
      margin: 0 3% 0 0;
      color: var(--inactive-tab);
      display: flex;
      flex-direction: column;
      width: auto;
      p {
        display: inline;
        width: auto;
      }
    }
    .select {
      color: var(--text-01) !important;
    }
    .underline {
      height: 2px;
      width: 100%;
      background: var(--line-active);
    }
    margin:  0 0 2% 0;
  }
}

</style>