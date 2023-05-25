<template>
  <div class="container community-form" id="background" style="width:600px;">
    <div class="row">
      <router-link class="col-1" :to="{name: 'Community' }">
        <img src="@/assets/back.png" style="width:25px;" alt="back">
      </router-link>
      <span class="col-10" style="text-align: center;"><h1>게시글 작성</h1></span>
    </div>
    <br>
    <form @submit.prevent="createCommunity">
      <div class="mb-3 py-3">
        <input type="text" class="form-control" aria-describedby="titleHelp" v-model.trim="title" placeholder="제목">
        <div id="titleHelp" class="form-text">100자 이하</div>
      </div>
      <div class="mb-3 py-3">
        <textarea type="text" class="form-control" id="content" v-model.trim="content" placeholder="내용" style="height: 500px;"></textarea>
      </div>
      <button type="submit" class="btn btn-primary btn-custom">등록</button>

    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityForm',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createCommunity() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요!')
        return
      } else if (!content) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/community_list_create/`,
        data: {
          title,
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.$router.push({ name: 'CommunityDetail', params: { community_pk: res.data.id }})
        })
        .catch(err => console.log(err))
    }
  }

}
</script>

<style>
.community-form {
  margin-bottom: 123px;
}

#background {
  color:aliceblue
}
.btn-custom {
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  font-weight: bold;
  text-transform: uppercase;
  background-color: #ff4081;
  border: none;
  color: #ffffff;
  transition: background-color 0.3s ease;
}

.btn-custom:hover {
  background-color: #f50057;
}

.btn-custom:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 64, 129, 0.4);
}

</style>
