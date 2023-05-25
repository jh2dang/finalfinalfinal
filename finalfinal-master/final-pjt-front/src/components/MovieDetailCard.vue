<template>
  <div class="movie-item p-0 col-auto g-3 mx-3 text-nowrap" @click="goMovie">
    <img :src="poster_path + movie.poster_path" alt="..." class="poster-image">
  </div>
</template>

<script>

export default {
  name: 'MovieDetailCard',
  props: {
    movie: Object,
  },
  data() {
    return {
      poster_path: 'https://image.tmdb.org/t/p/w300/'
    }
  },
  methods: {
    goMovie() {
      this.$router.push({ name: 'Movie', params: { title: this.movie.title }})
    }
  }
}
</script>

<style>
  .movie-item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
}

.movie-item:hover {
  cursor: pointer;
}

.popular-list .movie-item:focus,
.popular-list .movie-item:hover {
  transform: scale(1.4);
  z-index: 1;
}

.popular-list:focus-within ~ .movie-item,
.popular-list:hover ~ .movie-item {
  transform: translateX(-25%);
}

.movie-item:focus .movie-item,
.movie-item:hover .movie-item {
  transform: translateX(25%);
}

.poster-image {
  max-width: 150px; /* 수정된 부분: 포스터 이미지의 최대 너비를 지정 */
  height: auto;
}
</style>
