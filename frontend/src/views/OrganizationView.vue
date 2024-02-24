<template>
  <div class="organization">
    <p>Организация {{this.$route.params.nameOrganization}} </p>
    <h2>{{ $route.params.nameOrganization }}</h2>
    <div class="button">
      <button-main @clickEvent="isOpenDialog = true">
        Добавить проект</button-main
      >
    </div>
    <div class="tasks">
      <div @click="$router.push($route.params.nameOrganization + '/'+ task.title)" v-for="task in tasks" :key="task.title" class="task__item">
        <div class="item__title">{{ task.title }}</div>
        <div class="item__deadline">{{ task.deadline }}</div>
        <div class="item__members">{{ task.countMembers }}</div>
        <div class="item__countTasks">{{ task.countTasks }}</div>
      </div>
          <dialog-create-task @close-dialog="createNewTask" v-if="isOpenDialog">
    </dialog-create-task>
    </div>


  </div>
</template>

<script>
import DialogCreateTask from "../components/DialogCreateTask.vue";
import ButtonText from "../components/UI/ButtonText.vue";
import MyInput from "../components/UI/MyInput.vue";
import ButtonMain from "../components/UI/ButtonMain.vue";

export default {
    emits: ["input-event", "close-dialog"],
  components: {
    DialogCreateTask,
    MyInput,
    ButtonMain,
    ButtonText,
    ButtonText,
  },
  data() {
    return {
      tasks: {},
      isOpenDialog: false,
    };
  },
  methods: {
      createNewTask(newTask) {
      if (Object.keys(newTask  ).length != 0) {
          this.tasks.push(newTask);
      }
        this.isOpenDialog = false
      },
      getTasksByName() {
        const organization = this.$store.getters.getTasksByName(this.$route.params.nameOrganization.slice(1))
        this.tasks = organization.tasks
      }
  },
  mounted() {
   this.getTasksByName()

  },
  computed: {

  }
};
</script>

<style lang="scss" scoped>
.organization {
  padding: 0 5%;
}
.button {
  width: 20%;
}

.tasks {
  display: flex;
  flex-direction: column;
  .task__item {
    padding: 2%;

    display: flex;
    align-items: center;

    background: var(--base-02);
    border-radius: 8px;
    margin: 1% 0 0 0;
    // display: flex;

    height: 50px;
    white-space: nowrap;
    .item__title {
      width: 400px;
    }
    .item__deadline {
      margin-left: 25%;
    }
    .item__members {
      margin-left: 20%;
    }
    .item__countTasks {
      margin-left: 20%;
    }
  }
}
</style>