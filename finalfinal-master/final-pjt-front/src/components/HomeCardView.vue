<template>
  <swiper-slide role="tab">
    <div class="movie-item" @click="goDetail">
      <img :src="poster_path + movie.poster_path" alt="..." class="poster-image">
    </div>
  </swiper-slide>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'HomeCardView',
  props: {
    movie: Object,
  },
  components: {
    swiperSlide,
  },
  data() {
    return {
      poster_path: 'https://image.tmdb.org/t/p/w300/'
    }
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movie.movie_id }})
    }
  }
}
</script>

<style scoped>
.movie-item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
}

.poster-image {
  width: 100%;
  height: auto;
  max-width: 200px; /* 조정된 포스터 크기 */
  transition: transform 0.3s ease-in-out;
}

.movie-item:hover .poster-image {
  transform: scale(1.1);
}

.movie-item:focus .poster-image,
.movie-item:focus-within .poster-image,
.movie-item:hover .poster-image {
  transform: scale(1.1);
  z-index: 1;
}

.popular-list:focus-within ~ .movie-item,
.popular-list:hover ~ .movie-item,
.movie-item:focus .movie-item,
.movie-item:hover .movie-item {
  transform: translateX(-25%);
}

.popular-list .movie-item:focus,
.popular-list .movie-item:hover {
  transform: scale(1.4);
  z-index: 1;
}
</style>
