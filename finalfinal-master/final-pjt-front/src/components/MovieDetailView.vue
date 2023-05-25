<template>
<div>
    <div
      class="background-image"
      :style="{ backgroundImage: `url(${imageUrl}${movie?.poster_path})` }"
    ></div>

  <div class="movie-detail-card" style="padding-top: 100px">

    <!-- class="movie-detail-card-wrapper" -->
    <div>
      <div class="d-flex justify-content">
        <!-- 포스터 -->
        <div class="movie-detail-poster pe-4" v-if="movie">
          <img :src="this.imageUrl + movie?.poster_path" alt="포스터 없음" />
        </div>
        <!-- 포스터 끝 -->

        <!-- 영화 정보 -->
        <div class="container">
          <div class="row d-flex justify-content-between">
            <!-- 제목 & 별점 -->
            
            <span class="col-10 movie-detail-title" style="font-family: BMDOHYEON; line-height: 100%; margin-left: -7px; font-size:3rem">
              <p>{{ movie?.title }}</p>
            </span>

            <div class="col-2 d-flex justify-content-left">
              <img
                id="movie-star"
                src="@/assets/star.png"
                style="height: 50px"
              />
              <div class="movie-vote px-2">
                {{ movie?.vote_average }}
              </div>
            </div>

            <!-- 개봉일 -->
            <div v-if="movie?.release_date" class="movie-release-date">
              개봉 : {{ movie.release_date }}
            </div>
            <!-- 개봉일 끝 -->

            <!-- 줄거리 -->
            <div class="movie-detail-header">
              <p class="mb-1">줄거리</p>

              <hr class="my-1" />
              <div v-if="movie?.overview" class="movie-detail-body">
                {{ movie?.overview }}
              </div>
              <div v-else class="movie-detail-overview-body">
                해당 영화는 줄거리가 제공되지 않습니다.
              </div>
            </div>
            <!-- 줄거리 끝 -->

            <!-- 좋아요, 리뷰 작성 -->
            <div
              class="d-flex justify-content-end align-middle movie-detail-header"
            >
              <span
                class="d-flex align-items-baseline ms-2 p-2 heart-box"
                @click="like"
              >
                <i
                  v-if="isLiked"
                  class="bi bi-heart-fill heart"
                  style="height: 50px"
                  :class="{ animate: isLiked }"
                ></i>
                <i
                  v-else
                  class="bi bi-heart heart"
                  :class="{ animate: isLiked }"
                ></i>
                <p class="px-2">좋아요</p>
                <p class="ps-2">{{ this.likeNumber }}개</p>
              </span>

              <span
                class="d-flex justify-content-space-between ms-2 p-2 review-create"
                @click="reviewForm"
              >
                <img
                  class="pt-2 pb-0"
                  src="@/assets/plus.png"
                  style="height: 40px"
                />
                <p class="px-2">리뷰 쓰기</p>
              </span>
            </div>
            <!-- 좋아요, 리뷰작성 끝 -->
          </div>
        </div>
      </div>
    </div>
    <br />
    <br />
    <br />
    <!-- 탭 -->
    <!-- 탭 -->
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button
          class="nav-link active"
          id="home-tab"
          data-bs-toggle="tab"
          data-bs-target="#home-tab-pane"
          type="button"
          role="tab"
          aria-controls="home-tab-pane"
          aria-selected="true"
        >
          리뷰
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="profile-tab"
          data-bs-toggle="tab"
          data-bs-target="#profile-tab-pane"
          type="button"
          role="tab"
          aria-controls="profile-tab-pane"
          aria-selected="false"
        >
          관련 영상
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="contact-tab"
          data-bs-toggle="tab"
          data-bs-target="#contact-tab-pane"
          type="button"
          role="tab"
          aria-controls="contact-tab-pane"
          aria-selected="false"
        >
          추천 영화
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="similar-tab"
          data-bs-toggle="tab"
          data-bs-target="#similar-tab-pane"
          type="button"
          role="tab"
          aria-controls="similar-tab-pane"
          aria-selected="false"
        >
          비슷한 영화
        </button>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <div
        class="tab-pane fade show active"
        id="home-tab-pane"
        role="tabpanel"
        aria-labelledby="home-tab"
        tabindex="0"
      >
        <div v-if="movie">
          <ReviewList :movieId="movieId" :movie="movie" class="m-3" />
        </div>
      </div>
      <div
        class="tab-pane fade"
        id="profile-tab-pane"
        role="tabpanel"
        aria-labelledby="profile-tab"
        tabindex="0"
      >
        <div
          class="d-flex justify-content-start flex-wrap"
          v-if="youtubeVideos.length"
        >
          <YoutubeItem
            v-for="(youtube, idx) in youtubeVideos"
            :key="idx"
            :youtube="youtube"
          />
        </div>
        <div v-else class="text-center p-5">
          <h4>관련 영상이 없습니다.</h4>
        </div>
      </div>

      <div
        class="tab-pane fade"
        id="contact-tab-pane"
        role="tabpanel"
        aria-labelledby="contact-tab"
        tabindex="0"
      >
        <div class="row popular-list">
          <MovieDetailCard
            v-for="movie in cosMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </div>
      </div>

      <div
        class="tab-pane fade"
        id="similar-tab-pane"
        role="tabpanel"
        aria-labelledby="similar-tab"
        tabindex="0"
      >
        <div class="row popular-list">
          <MovieDetailCard
            v-for="movie in similarMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import ReviewList from "@/components/review/ReviewList";
import axios from "axios";
import MovieDetailCard from "./MovieDetailCard.vue";
import YoutubeItem from "@/components/YoutubeItem.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  components: {
    ReviewList,
    MovieDetailCard,
    YoutubeItem,
  },
  data() {
    return {
      imageUrl: "https://image.tmdb.org/t/p/original",
      youtubeEmbeded: "https://www.youtube.com/embed",
      movieId: this.$route.params.movie_id.toString(),
      movie: null,
      isLiked: false,
      me: null,
      likeNumber: "",
      cosMovies: this.$store.state.cosMovies,
      similarMovies: this.$store.state.similarMovies,
      isLogin: this.$store.getters.isLogin,
    };
  },
  computed: {
    recoMovies() {
      return this.$store.state.cosMovies;
    },
    youtubeVideos() {
      return this.$store.state.youtubeVideos;
    },
  },
  created() {
    this.getMovie(this.$route.params.movie_id);
    this.getMe();
    this.getCosMovie();
    this.getSimilarMovie();
    this.searchYoutube();
  },
  methods: {
    reviewForm() {
      if (this.isLogin === false) {
        alert("리뷰 작성을 하시려면 로그인을 하세요!");
        return;
      }
      this.$router.push({
        name: "ReviewForm",
        params: {
          movie_id: this.movieId,
          movie_pk: this.movie.id,
        },
      });
    },
    getCosMovie() {
      this.$store.dispatch("getCosMovie", this.movieId); // 디테일 페이지의 영화 id
    },
    getSimilarMovie() {
      this.$store.dispatch("getSimilarMovie", this.movieId);
    },
    getMovie(movieId) {
      // console.log(movieId)
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/`,
        data: {
          movie_id: movieId,
        },
      })
        .then((res) => {
          // console.log(res.data)
          this.movie = res.data;
          this.likeNumber = this.movie.like_users.length;
        })
        .catch((err) => {
          console.log(err);
          this.$router.push({ name: "NotFound404" });
        });
    },
    searchYoutube() {
      this.$store.dispatch("searchYoutube", this.movieId);
    },
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
        this.islike();
      });
    },
    like() {
      if (this.isLogin === false) {
        alert("좋아요 하려면 먼저 로그인 해 주세요.");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.me.pk}/${this.movieId}/like/`,
        data: {
          myId: this.me.id,
          movieId: this.movie.id,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.isLiked = res.data;
        if (this.isLiked === false) {
          this.likeNumber -= 1;
        } else {
          this.likeNumber += 1;
        }
      });
    },
    islike() {
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.me.pk}/${this.movieId}/is_liked/`,
        data: {
          myId: this.me.id,
          movieId: this.movieId,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.isLiked = res.data;
      });
    },
  },
};
</script>

<style scoped>
@font-face {
  font-family: "SUITE-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
}

.container {
  font-family: "SUITE-Regular";

}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  filter: blur(10px) brightness(40%);
  z-index: 1;
}

.movie-detail-card-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.5); /* 반투명한 하얀색 배경 */
  border-radius: 5%; /* 동그란 테두리 */
  padding: 20px; /* 필요한 패딩 */
  position: relative;
  z-index: 1;
}

.movie-detail-card {
  position: relative;
  overflow: hidden;
  font-family: "Noto Sans KR", sans-serif;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  padding: 50px 15%;
  min-height: 100%;
  height: auto;
  z-index: 1;
  /* background-color: #000000; */
  /* color: white; */
}

.movie-detail-toolbar {
  height: 56px;
}

/* .movie-detail-body {
  display: flex;
  flex-flow: row wrap;
  margin: 1rem;
} */

.movie-detail-info {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  margin: 1rem 0 0 4rem;
  width: 60%;
}

.movie-detail-info-header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  height: 80px;
}

.movie-detail-poster > img {
  width: 400px;
}

.movie-detail-title {
  font-size: 40px;
  font-weight: bolder;
}

.movie-detail-info-header-right {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.movie-vote {
  font-size: 30px;
}

#movie-star {
  height: 50%;
  margin-left: 1rem;
}

.movie-detail-header {
  margin-top: 5rem;
  padding-top: 5rem;
  font-size: 32px;
}

.movie-detail-body {
  font-size: 20px;
}
.heart {
  color: crimson;
  margin: 0px auto;
  -webkit-transition-duration: 0.4s;
  transition-duration: 0.4s;
}

.heart-box,
.review-create {
  cursor: pointer;
}
.tab-pane {
  margin-top: 20px;
}

.tab-pane .d-flex {
  margin-bottom: 20px;
}

.tab-pane .d-flex .youtube-item {
  flex-basis: 33.33%;
  max-width: 33.33%;
  padding: 10px;
  box-sizing: border-box;
}

.tab-pane .d-flex .youtube-item .thumbnail {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
  overflow: hidden;
}

.tab-pane .d-flex .youtube-item .thumbnail img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.tab-pane .d-flex .youtube-item .title {
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
}

.tab-pane .text-center {
  text-align: center;
}

.tab-pane .p-5 {
  padding: 5px;
}
.animate {
  animation-name: heartbeat;
  animation-duration: 0.5s;
  animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  animation-iteration-count: 1;
  transform-origin: center;
}

@keyframes heartbeat {
  0% {
    transform: scale(1);
  }
  10% {
    transform: scale(1.3);
  }
  30% {
    transform: scale(0.9);
  }
  50% {
    transform: scale(1.2);
  }
  70% {
    transform: scale(0.95);
  }
  90% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
