<template>
<div class="login">
  <div class="container">
    <div class="card" id="login" style="background-color: rgba(0, 0, 0, 0.6);">
      <div class="card-body d-flex flex-column align-items-center">
  <h1 class="card-title text-white fw-bold">LOGIN</h1>
  <br>
  <form @submit.prevent="logIn">
    <div class="form-group">
      <label for="username" class="card-subtitle mb-2 text-white">아이디</label><br>
      <input type="text" id="username" v-model="username" class="form-control text-white" style="border:none; background: rgba(0, 0, 0, 0.5);">
    </div>
    <br>
    <div class="form-group">
      <label for="password" class="card-subtitle mb-2 text-white">비밀번호</label><br>
      <input type="password" id="password" v-model="password" class="form-control text-white" style="border:none; background: rgba(0, 0, 0, 0.5);">
    </div>
    <br>
    <div class="form-group">
      <button type="submit" class="btn bg-white btn-block">로그인</button>
    </div>
  </form>
  <hr>
  <p class="text-white text-center">아직 하나비의 회원이 아니신가요?<br>
    <router-link :to="{ name: 'Signup'}" class="d-flex justify-content-center" style="text-decoration:none;">가입하러 가기 ></router-link>
  </p>
</div>

    </div>
  </div>

</div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
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

#login {
  width: 400px;
  border-radius: 10px;
  background-color: #f2f2f2;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  padding: 20px;
}

.login {
  background-image: url('@/assets/login.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

/* 



.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.card {
  max-width: 400px;
  border-radius: 10px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.card-body {
  padding: 2rem;
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

p {
  margin-top: 10px;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  color: #0056b3;
  text-decoration: underline;
} */
</style>
