<template>
  <header>
    <nav>
      <div class="nav_left">
        <img class="nav__item" src="../assets/logo.png" alt="" />
        <router-link class="nav__item" to="Organizations"
          >Организации</router-link
        >
        <router-link class="nav__item" to="chat">Чаты</router-link>
        <router-link class="nav__item" to="about">О сервисе</router-link>
      </div>
      <div class="nav_right">
        <div class="search nav__item">
          <button class="search__btn">
            <img src="../assets/icons/Icons.svg" alt="" />
          </button>
          <!-- <input type="text" placeholder="Поиск" class="search__form" /> -->
        </div>
        <div class="nav__item">
          <button>
            <img class="" src="../assets/icons/notification.svg" alt="" />
          </button>
        </div>
        
        <router-link class="nav__item" to="profile">Личный кабинет</router-link>
      </div>

    </nav>
  </header>
</template>

<script setup >
defineProps({
  isHorizontal: Boolean,
});
</script>

<style lang="scss" scoped>
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2% 5%;
  nav {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .nav_left, .nav_right {
      display: flex;
      align-items: center;
    }
    .nav_left {
      display: flex;
      align-items: center;
    }
    .nav__item {
      margin: 0 6% 0 0%;
      color: black;
      text-decoration: none;
      white-space: nowrap;
      button {
        background: none;
        border: none;
        cursor: pointer;
      }

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
}
</style>