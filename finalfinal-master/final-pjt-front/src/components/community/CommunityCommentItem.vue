<template>
  <div>
    <div v-if="update">
      <div class="comment-header">
        <div class="comment-username">
          <p @click="goProfile" class="fw-bold fs-5">{{ comment.userName }}</p>
        </div>
        <div v-if="this.me.username === comment.userName">
          <div class="comment-buttons">
            <button class="btn btn-edit btn-sm" @click="updateForm">수정</button>
            <button class="btn btn-delete btn-sm" @click="deleteComment">삭제</button>
          </div>
        </div>
      </div>
      <p>{{ comment.content }}</p>
      <hr>
    </div>

    <div v-else>
      <p>{{ comment.userName }}</p>
      <form @submit.prevent="updateComment">
        <div>
          <input type="text" v-model.trim="updateContent" value="content" />
          <div class="button-group">
            <button class="btn btn-submit" type="submit">등록</button>
            <button class="btn btn-cancel" @click="cancelUpdate">취소</button>
          </div>
        </div>
      </form>
    </div>
    <hr class="divider" />
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityCommentItem",
  props: {
    comment: Object,
    communityId: String,
  },
  data() {
    return {
      update: true,
      updateContent: this.comment.content,
      me: [],
    };
  },
  created() {
    this.getMe();
  },
  methods: {
    getMe() {
      if (this.$store.getters.isLogin === false) {
        return;
      }
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.me = res.data;
      });
    },
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/community/comment/${this.communityId}/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(() => {
        this.$emit("del_comment");
      });
    },
    updateForm() {
      this.update = !this.update;
    },
    cancelUpdate() {
      this.update = !this.update;
    },
    updateComment() {
      const updateContent = this.updateContent;
      axios({
        method: "put",
        url: `${API_URL}/community/comment/${this.communityId}/${this.comment.id}/`,
        data: {
          content: updateContent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(() => {
        this.update = !this.update;
        this.$emit("update_comment");
      });
    },
    goProfile() {
      this.$router.push({
        name: "Profile",
        params: { user_pk: this.comment.user },
      });
    },
  },
};
</script>

<style>
.container {
  margin-bottom: 10px;
}

.comment-header {
  display: flex;
  align-items: center;
  /* justify-content: space-between; */
  margin-bottom: 5px;
}

.comment-username {
  cursor: pointer;
}

.comment-buttons {
  display: flex;
}

.comment-buttons .btn {
  margin-right: 5px;
  color: white;
}

.comment-buttons .btn-edit {
  background-color: #007bff;
}

.comment-buttons .btn-delete {
  background-color: #dc3545;
}

.divider {
  border-top: 1px solid #ccc;
  margin-top: 10px;
  margin-bottom: 10px;
}

.button-group {
  display: flex;
  align-items: center;
}

.button-group .btn {
  margin-right: 5px;
  color: white;
}

.button-group .btn-submit {
  background-color: #28a745;
}

.button-group .btn-cancel {
  background-color: #dc3545;
}

.btn {
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  opacity: 0.8;
}

/* .comment-divider {
  border-top: 2px dashed #ccc;
  margin-top: 20px;
  margin-bottom: 20px;
} */
</style>
