<template>
  <div class="signup">
    <div class="container p-5">
      <div class="card col-md-6 m-auto p-3" id="signup" style="background-color: rgba(0, 0, 0, 0.6);">
        <div class="card-body d-flex flex-column align-items-center">
  <h1 class="card-title text-white fw-bold">SIGN UP</h1>
  <br>
  <form @submit.prevent="signUp">
    <div class="form-group">
      <label for="username" class="card-subtitle mb-2 text-white">아이디</label><br>
      <input type="text" id="username" v-model="username" class="form-control text-white" style="border:none; background: rgba(0, 0, 0, 0.5);">
    </div>
    <br>
    <div class="form-group">
      <label for="password1" class="card-subtitle mb-2 text-white">비밀번호</label><br>
      <input type="password" id="password1" v-model="password1" class="form-control text-white" style="border:none; background: rgba(0, 0, 0, 0.5);">
    </div>
    <br>
    <div class="form-group">
      <label for="password2" class="card-subtitle mb-2 text-white">비밀번호 재확인</label><br>
      <input type="password" id="password2" v-model="password2" class="form-control text-white" style="border:none; background: rgba(0, 0, 0, 0.5);">
    </div>
    <br>
    <div class="form-group d-flex justify-content-center">
      <button type="submit" class="btn bg-white btn-block">회원가입</button>
    </div>
  </form>
  <hr>
  <p class="py-1 text-white text-center">이미 하나비의 회원이신가요?<br>
    <router-link :to="{ name: 'Login'}" class="d-flex justify-content-center" style="text-decoration:none;">로그인하러 가기 ></router-link>
  </p>
</div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    },
  }
}
</script>

<style scoped>

@font-face {
    font-family: 'SEBANG_Gothic_Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/SEBANG_Gothic_Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

h1 {
  font-family: 'SEBANG_Gothic_Bold';
}

router-link {
  text-decoration: none;
}

#signup {
  width: 400px;
  border-radius: 10px;
  background-color: #f2f2f2;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  padding: 20px;
}

.signup {
  background-image: url('@/assets/login.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}




.form-group {
  margin-bottom: 20px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0069d9;
  border-color: #0062cc;
}

.btn-primary:focus,
.btn-primary.focus {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}

.btn-block {
  display: block;
  width: 100%;
}

.py-1 {
  margin-top: 10px;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  color: #0056b3;
  text-decoration: underline;
}
</style>
