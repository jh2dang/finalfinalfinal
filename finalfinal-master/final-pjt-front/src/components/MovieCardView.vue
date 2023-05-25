<template>
  <div
    class="movie-item p-0 col-auto g-3 mx-3"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
    @click="goDetail"
  >
    <img :src="poster_path + movie.poster_path" alt="..." class="img-fluid poster-image" style="width: 250px; border-radius: 10px;">
  </div>
</template>


<script>
export default {
  name: 'MovieCardView',
  props: {
    movie: Object,
  },
  data() {
    return {
      poster_path: 'https://image.tmdb.org/t/p/w300/',
      isHovered: false
    }
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movie.movie_id }})
    },
    handleMouseEnter() {
      this.isHovered = true;
    },
    handleMouseLeave() {
      this.isHovered = false;
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
.popular-list .movie-item:hover,
.movie-item.is-hovered {
  transform: scale(1.4);
  z-index: 1;
}

.popular-list:focus-within ~ .movie-item,
.popular-list:hover ~ .movie-item,
.movie-item.is-hovered ~ .movie-item {
  transform: translateX(-25%);
}

.movie-item:focus .movie-item,
.movie-item:hover .movie-item,
.movie-item.is-hovered .movie-item {
  transform: translateX(25%);
}

.poster-image {
  max-width: 120px; /* 수정된 부분: 포스터 이미지의 최대 너비를 지정 */
  height: auto;
}

/* Responsive Styles */
@media (max-width: 576px) {
  .movie-item {
    flex-basis: 50%;
  }
}

@media (min-width: 577px) and (max-width: 768px) {
  .movie-item {
    flex-basis: 33.33%;
  }
}

@media (min-width: 769px) and (max-width: 992px) {
  .movie-item {
    flex-basis: 25%;
  }
}

@media (min-width: 993px) {
  .movie-item {
    flex-basis: 20%;
  }
}
</style>

