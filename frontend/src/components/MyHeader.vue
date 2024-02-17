<template>
  <header>
    <nav>
      <div class="nav_left">
        <img class="nav__item" src="../assets/logo.png" alt="" />
        <router-link tag="button" class="nav__item" to="Organizations">Организации</router-link>
        <router-link tag="button"  class="nav__item" to="" v-if="$store.state.isAuthorized" >Чаты</router-link>
        <p class="nav__item disabled "  v-else >Чаты</p>

        <router-link tag="button" class="nav__item" to="">О сервисе</router-link>
      </div>
      <div class="nav_right">
        <div class="search nav__item">
          <!-- <button class="search__btn">
            <img src="../assets/icons/Icons.svg" alt="" />
          </button> -->
          <!-- <input type="text" placeholder="Поиск" class="search__form" /> -->
        </div>
        <div class="nav__item">
          <button >
            <img class="nav__bell" :src="( disabledIconPath)" />
          </button>
        </div>
        
        <router-link tag="button" v-if="$store.state.isAuthorized" class="nav__item" to="profile">Личный кабинет</router-link>
        <router-link tag="button" v-else class="nav__item" to=""> Вход / Регистрация</router-link>

      </div>
    </nav>
    <div class="line" ></div>

  </header>

</template>

<script >
export default {

  data() {
    return {

    };
  },
  computed: {
    disabledIconPath() {
      if (this.$store.state.isAuthorized) {
        return new URL('../assets/icons/Type=Bell, State=Default.svg' , import.meta.url).href

      }else {
        return new URL('../assets/icons/Type=Bell, State=Disabled.svg' , import.meta.url).href

      }

    }

  }
};
</script>

<style lang="scss" scoped>
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
  padding: 2% 5%;
  nav {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    // flex-direction: column;
    .nav_left, .nav_right {
      display: flex;
      align-items: center;
    }
    .nav_right {
      justify-content: flex-end;
    }
    .nav__item {
      margin: 0 6% 0 0%;
      text-decoration: none;
      white-space: nowrap;
      color: var(--text-01) ;

      button {
        background: none;
        border: none;
        cursor: pointer;
      }

    }
    .disabled {
      color: var(--text-02);
      cursor: default;
    }

    .search {
      display: flex;
      align-items: center;
      border-radius: 8px;
      .search__form {
        height: 100%;
        border: none;
      }
      .search__form:focus {
        outline: 0;
      }
    }

  }
    .line {
      width: 100%;
      height: 2px;
      background: var(--line-main);
    }
}
</style>