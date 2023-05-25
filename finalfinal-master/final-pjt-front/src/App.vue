<template>
  <div id="app">
    <nav
      class="navbar text-white"
      style="position: fixed; z-index: 99; width: 100%; height: 3rem"
    >
      <div class="mx-2"><img src="@/assets/logo.png" alt="" style="width: 40px" /></div>
      <div>
        <div v-if="!isLogin">
          <router-link
            :to="{ name: 'Signup' }"
            class="text-white text-decoration-none mx-2"
            >회원가입</router-link
          >
          <router-link
            :to="{ name: 'Login' }"
            class="text-white text-decoration-none mx-2"
            >로그인</router-link>
        </div>


        <div v-else>
          <router-link
            class="text-white text-decoration-none mx-2 d-inline"
            :to="{ name: 'MyProfile', params: { username: username } }"
            >내 프로필</router-link
          >
          <p role="button" @click="logOut" class="d-inline mx-2">로그아웃</p>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row flex-nowrap">
        
        <!-- 여기부터 사이드바 -->
        <div
          class="sidebar col-auto px-sm-5 px-0 mt-5"
          style="position: fixed; z-index: 99;"
        >
          <div
            class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-5 text-white min-vh-100"
          >
            <div v-if="!isLogin">
              <img
                src="https://mblogthumb-phinf.pstatic.net/MjAyMDExMDFfMyAg/MDAxNjA0MjI5NDA4NDMy.5zGHwAo_UtaQFX8Hd7zrDi1WiV5KrDsPHcRzu3e6b8Eg.IlkR3QN__c3o7Qe9z5_xYyCyr2vcx7L_W1arNFgwAJwg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EC%8A%A4%ED%85%94.jpg?type=w800"
                alt="..."
                width="150"
                height="150"
                class="rounded-circle mb-3 d-none d-sm-inline"
              />
              <hr />
            </div>

            <div v-else>
              <img
                src="@/assets/jeje.jpg"
                alt="hugenerd"
                width="150"
                height="150"
                class="rounded-circle mb-3 d-none d-sm-inline"
              />
              <br />
              <p class="fs-6 d-none d-sm-inline">
                안녕하세요, {{ this.$store.state.username }}님!
              </p>
              <hr />
            </div>
            <ul
              class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
              id="menu"
            >
              <li class="nav-item">
                <router-link
                  :to="{ name: 'Home' }"
                  class="nav-link align-middle px-0 text-white"
                >
                  <i class="fs-4 bi-house"></i>
                  <span class="ms-1 d-none d-sm-inline">Home</span></router-link
                >

                <!-- </a> -->
              </li>
              <li class="nav-item">
                <router-link
                  :to="{ name: 'Movie' }"
                  class="nav-link px-0 align-middle text-white"
                >
                  <i class="fs-4 bi-search"></i>
                  <span class="ms-1 d-none d-sm-inline"
                    >Search</span
                  ></router-link
                >
              </li>
              <li class="nav-item">
                <a
                  href="#submenu1"
                  data-bs-toggle="collapse"
                  class="nav-link px-0 align-middle text-white"
                >
                  <i class="fs-4 bi-people"></i>
                  <span class="ms-1 d-none d-sm-inline">Community</span>
                </a>
                <ul
                  class="collapse show nav flex-column ms-1"
                  id="submenu1"
                  data-bs-parent="#menu"
                >
                  <li class="w-100">
                    <router-link
                      :to="{ name: 'Community' }"
                      class="nav-link px-0 text-white"
                    >
                      <span class="d-none d-sm-inline"
                        >ㄴ 자유게시판</span
                      ></router-link
                    >
                  </li>
                </ul>
              </li>
              <li class="nav-item">
                <a
                  href="#submenu2"
                  data-bs-toggle="collapse"
                  class="nav-link px-0 align-middle text-white"
                >
                  <i class="fs-4 bi-film"></i>
                  <span class="ms-1 d-none d-sm-inline">Cinema</span>
                </a>
                <ul
                  class="collapse show nav flex-column ms-1"
                  id="submenu2"
                  data-bs-parent="#menu"
                >
                  <li class="w-100">
                    <router-link
                      :to="{ name: 'CinemaNow' }"
                      class="nav-link px-0 text-white"
                    >
                      <span class="d-none d-sm-inline"
                        >ㄴ 현재 상영작</span
                      ></router-link
                    >
                  </li>
                  <li class="w-100">
                    <router-link
                      :to="{ name: 'CinemaUpcoming' }"
                      class="nav-link px-0 text-white"
                    >
                      <span class="d-none d-sm-inline"
                        >ㄴ 상영 예정작</span
                      ></router-link
                    >
                  </li>
                </ul>
              </li>
              <li class="nav-item">
                <router-link
                  :to="{ name: 'OttViewHome' }"
                  class="nav-link align-middle px-0 text-white"
                >
                  <i class="fs-4 bi-house"></i>
                  <span class="ms-1 d-none d-sm-inline">OTT</span></router-link
                >

                <!-- </a> -->
              </li>
            </ul>
            <hr />
            <div v-if="!isLogin">
              <img
                src="https://mblogthumb-phinf.pstatic.net/MjAyMDExMDFfMyAg/MDAxNjA0MjI5NDA4NDMy.5zGHwAo_UtaQFX8Hd7zrDi1WiV5KrDsPHcRzu3e6b8Eg.IlkR3QN__c3o7Qe9z5_xYyCyr2vcx7L_W1arNFgwAJwg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EC%8A%A4%ED%85%94.jpg?type=w800"
                alt="..."
                width="30"
                height="30"
                class="rounded-circle mb-3 d-none d-sm-inline"
              />
              <span class="ml-2 d-none d-sm-inline">로그인 해 주세요.</span>
            </div>
            <div class="dropdown pb-4 mb-5" v-else>
              <a
                href="#"
                class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
                id="dropdownUser1"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <img
                  src="@/assets/jeje.jpg"
                  alt="hugenerd"
                  width="30"
                  height="30"
                  class="rounded-circle"
                />
                <span class="d-none d-sm-inline mx-1">{{
                  this.$store.state.username
                }}</span>
              </a>
              <ul class="dropdown-menu dropdown-menu-dark text-small shadow">
                <li><a class="dropdown-item" href="#">Settings</a></li>
                <li>
                  <router-link
                    class="dropdown-item"
                    :to="{ name: 'MyProfile', params: { username: username } }"
                    >Profile</router-link
                  >
                </li>
                <li>
                  <hr class="dropdown-divider" />
                </li>
                <li>
                  <button class="dropdown-item" @click="logOut">
                    Sign out
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div
          class="col py-3"
          style="margin-top: 2rem; margin-left: 291px; overflow: auto"
        >
          <router-view></router-view>
        </div>
      </div>
    </div>
    <footer></footer>
  </div>
</template>

<script>
export default {
  computed: {
    username() {
      return this.$store.state.username;
    },
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    logOut() {
      this.$store.commit("LOGOUT");
    },
    logIn() {
      this.$router.push({ name: "Login" });
    },
    signUp() {
      this.$router.push({ name: "Signup" });
    },
  },
};
</script>

<style>
@font-face {
  font-family: "SUITE-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
}

#app {
  font-family: "SUITE-Regular";
  background-color: rgb(33, 37, 41);
  color: aliceblue;
}




.navbar {
  background-color: rgba(0, 0, 0, 0.685);
}

.sidebar {
  background-color: rgb(10, 12, 13);

}

@media (min-width: 576px) {
  .col-lg-3 {
    flex: 0 0 auto;
    width: 250px;
    max-width: 250px;
  }
}

@media (max-width: 575.98px) {
  .col-auto {
    flex: 0 0 auto;
    width: 100%;
    max-width: 100%;
  }
}

.position-fixed {
  position: fixed !important;
}

.position-relative {
  position: relative !important;
}
</style>
