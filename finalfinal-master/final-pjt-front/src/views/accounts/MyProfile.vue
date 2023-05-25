<template>
  <div class="container" style="padding-top:48px;padding-left:48px;">
    <div class="container" style="margin-bottom:30px">
      <div class="row">
          <div class="well profile">
            <div class="row">
              <div class="col-sm-3 col-12">
                <img src="@/assets/jeje.jpg" alt="profile" class="rounded-circle" style="width:250px;">
              </div>
              <div class="col-sm-9 col-12">
                <div class="col-12 d-flex justify-content-around">
                  <h1 class="title-font fw-bold" style="margin-bottom: 30px"><span style="font-size:5rem;">{{ user.username }}</span> 님의 프로필</h1>
                </div>
                <div class="col-sm-12 divider text-center row d-flex justify-content-around">
                  <div class="col-sm-3 col-12 follow-info" @click="open1">
                    <h2 class="fw-bold" style="font-size:3rem;">{{followersLength}}</h2>                    
                    <p>팔로워</p>
                  </div>
                  <div class="col-sm-3 col-12 follow-info"  @click="open2">
                    <h2 class="fw-bold" style="font-size:3rem;">{{followingsLength}}</h2>                    
                    <p>팔로잉</p>
                  </div>
                  <div class="col-sm-4 col-12">
                    <h2 class="fw-bold" style="font-size:3rem;">{{ user.like_movies.length }}</h2>                    
                    <p>좋아요한 영화 수</p>
                  </div>
              </div>
            </div>
            <div class="row ms-4 py-4">
              <div v-if="isFollowing" class="">{{ user.username }}님을 팔로우 중 입니다.</div>
              <div v-else><br></div>
            </div>    
            <div class="row mx-2">
              <div v-if="isLogin">
                <div v-if="me.username === user.username">
                  <!-- <br> -->
                </div>
                <div class="py-2" v-else>
                  <div class="d-grid gap-2 col-3 mx-auto">
                    <button v-if="isFollowing" @click="follow" class="btn btn-secondary">언팔로우</button>
                    <button v-else @click="follow" class="btn btn-primary">팔로우</button>
                  </div>
                </div>
              </div>
              <!-- <div v-else> </div> -->
            </div>        
          </div>
        </div>                 
      </div>
    </div>
    <!-- 팔로잉 모달 -->
    <b-modal
      hide-footer
      v-model="show2"
      id="review-modal"
      size="sm"
      title="팔로잉"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <section class="page-section" id="contact">
        <div class="control-group">
            <div v-for="(userId, idx) in user.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                <FollowingsView :userId="userId" />
            </div>
        </div>
      </section>
    </b-modal>
    <!-- 팔로잉 모달 끝 -->

    <!-- 팔로워 모달 -->
    <b-modal
      hide-footer
      v-model="show1"
      id="review-modal"
      size="md"
      title="팔로워"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <section class="page-section" id="contact">
        <div class="control-group">
            <div v-for="(userId, idx) in user.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                <FollowersView :userId="userId" />
            </div>
        </div>
      </section>
    </b-modal>
    <!-- 팔로워 모달 끝 -->

    <!-- 탭 -->
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button"
          role="tab" aria-controls="home-tab-pane" aria-selected="true">좋아요 영화</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button"
          role="tab" aria-controls="profile-tab-pane" aria-selected="false">리뷰 영화</button>
      </li>

    </ul>
    <div class="tab-content mt-4 rounded" id="myTabContent" style="background-color:rgba(0, 0, 0, 0.3);">
      <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
        <br>
        <h2 class="title-font ml-4">{{ user.username }}님이 좋아요 한 영화</h2>    
        <ul v-if="likeMovies" class="row popular-list">
          <MovieCardView
            v-for="movie in likeMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </ul>

      </div>
      <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
        <br>
        <h2 class="title-font ml-4">{{ user.username }}님이 리뷰한 영화</h2>    
        <ul v-if="reviewMovies" class="row popular-list">
          <MovieCardView
            v-for="movie in reviewMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </ul>

      </div>
    </div>
    <div style="height:300px;"></div>

  </div>
</template>


<script>
import axios from "axios";

import MovieCardView from "@/components/MovieCardView";
import FollowersView from "@/components/FollowersView.vue";
import FollowingsView from "@/components/FollowingsView.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MyProfile",
  data: function () {
    return {
      me: [],
      user: [],
      show1: false,
      show2: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
      likeMovies: [],
      reviewMovies: [],
    };
  },
  created() {
    this.getMe();
  },
  components: {
    MovieCardView,
    FollowersView,
    FollowingsView,
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
        this.getMyName(res.data.pk);
      });
    },
    getMyName(my_pk) {
      axios({
        method: "get",
        url: `${API_URL}/userinfo/user/${my_pk}/`,
      }).then((res) => {
        this.user = res.data;
        this.getUserMovies(res.data.like_movies, res.data.reviews);
      });
    },
    getUserMovies(like_movies, reviews) {
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.user.id}/like/review/`,
        data: {
          like_movies,
          reviews,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.likeMovies = res.data[0];
        this.reviewMovies = res.data[1];
      });
    },
    open1: function () {
      this.show1 = true;
    },
    open2: function () {
      this.show2 = true;
    },
    close: function () {
      this.show1 = false;
    },
    close2: function () {
      this.show2 = false;
    },
  },
  computed: {
    followingsLength: function () {
      if (this.user.followings) {
        return this.user.followings.length;
      } else {
        return 0;
      }
    },
    followersLength: function () {
      if (this.user.followers) {
        return this.user.followers.length;
      } else {
        return 0;
      }
    },
  },
};
</script>

<style scoped>

.center {
    position: relative;
    top: 50px;
}


.profile 
{
min-height: 355px;
display: inline-block;
}
.divider 
{
border-top:1px solid rgba(0, 0, 0, 0);
}
.emphasis 
{
border-top: 4px solid transparent;
}
.emphasis:hover 
{
border-top: 4px solid #1abc9c;
}
.emphasis h2
{
margin-bottom:0;
}
.follow-info:hover {
  cursor: pointer;
}
span.tags 
{
background: #404242;
border-radius: 2px;
color: #f5f5f5;
font-weight: bold;
padding: 4px 6px;
}
.container {
  padding-top: 48px;
  padding-left: 48px;
}
</style>