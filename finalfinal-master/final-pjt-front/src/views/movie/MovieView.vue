<template>
  <div class="movie-card">
    <div class="d-flex justify-content-center">
      <main>
        <h1>영화 검색하기</h1>
        
        <div class="SearchBox" style="background-color: rgba(0, 0, 0, 0.315);">
          <input
            type="text"
            class="SearchBox-input opacity-75"
            placeholder="영화제목을 입력하세요."
            v-model="title"
            @input="searchMovie"
          />
      
          <div class="SearchBox-button bg-danger" role="button" @click="searchMovie">
            <i class="SearchBox-icon material-icons">search</i>
          </div>
        </div>
      </main>
    </div>
      <div class="popular-list row gy-4 mx-auto mt-2 justify-content-center" v-if="movies">
        <MovieCardView
          v-for="movie in movies"
          :key="movie.created_at"
          :movie="movie"
        />
      </div>
    <div v-show="movies?.length === 0">
      <div class="text-center pt-5">
        <img src="@/assets/nothing.png" alt="없어요" />
        <p class="p-5 h1">찾으시는 영화가 없습니다</p>
      </div>
    </div>
    <br /><br /><br /><br />
    <div v-show="!title">
      <b-pagination
  @input="getList"
  v-model="currentPage"
  :total-rows="total_row"
  :per-page="perPage"
  aria-controls="my-table"
  align="center"
  class="pagination-wrapper text-decoration-none"
  :prev-text="`prev`"
  :next-text="`next`"
  :hide-goto-end-buttons="true"
  :hide-ellipsis="true"
>
</b-pagination>



      <b-table
        id="my-table"
        :movies="movies"
        :per-page="perPage"
        :current-page="currentPage"
        small
      ></b-table>
    </div>
  </div>
</template>

<script>
import MovieCardView from "@/components/MovieCardView";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieView",
  components: {
    MovieCardView,
  },
  data() {
    return {
      title: null,
      movies: null,
      // list: [],
      currentPage: 1,
      perPage: 5,
      total_row: 20,
      notMovies: false,
    };
  },
  created() {
    this.getList();
  },
  methods: {
    getList() {
      // console.log(this.currentPage)
      axios({
        methods: "get",
        url: `${API_URL}/movies/list/?page=${this.currentPage}`,
      }).then((res) => {
        // console.log(res)
        this.movies = res.data.results;
        this.total_row = parseInt(res.data.count / 20);
        this.searchCardMovie();
      });
    },
    searchMovie() {
      const moviedata = this.$store.state.movies;
      if (this.title) {
        const searchMovies = moviedata.filter((movie) => {
          return movie.title.includes(this.title);
        });
        this.movies = searchMovies;
      } else {
        this.getList();
      }
    },
    searchCardMovie() {
      if (this.$route.params.title) {
        this.title = this.$route.params.title;
        this.$route.params.title = null;
        const moviedata = this.$store.state.movies;
        if (this.title) {
          const searchMovies = moviedata.filter((movie) => {
            return movie.title.includes(this.title);
          });
          this.movies = searchMovies;
        }
      }
    },
  },
};
</script>

<style>
.movie-card {
  padding: 5% 5%;
}
.popular-list {
  display: flex;
  margin-left: 5rem;
  margin-right: 5rem;
}
.movie-card form {
  display: flex;
  align-items: center;
}

.movie-card input[type="search"] {
  flex-grow: 1;
  margin-right: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 2px solid #87cefa; /* Updated border color to light blue */
}

.movie-card button {
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  background-color: #007aff;
  color: white;
}

.movie-card button:hover {
  cursor: pointer;
}
:root {
  --primary-color: #081516;
  --accent-color: #f50057;

  --text-color: #263238;
  --body-color: #80deea;
  --main-font: 'Roboto';
  --font-bold: 700;
  --font-regular: 400;
}

* {
  box-sizing: border-box;
}

body {
  color: var(--text-color);
  background-color: var(--body-color);
  font-family: var(--main-font), Arial;
  font-weight: var(--font-regular);
}

main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 20vh;
}

h1 {
  font-weight: var(--font-bold);
}

input,
button {
  border: none;
  background: none;
  outline: 0;
}

button {
  cursor: pointer;
}

.SearchBox-input::placeholder {
  color: white;
  opacity: 0.6;
}

/* Chrome, Opera, and Safari */
.SearchBox-input::-webkit-input-placeholder {
  color: white;
}

/* Firefox 19+ */
.SearchBox-input::-moz-placeholder {
  color: white;
}

/* IE 10+ and Edge */
.SearchBox-input:-ms-input-placeholder {
  color: white;
}

/* Firefox 18- */
#formGroupExampleInput:-moz-placeholder {
  color: white;
}

.SearchBox {
  --height: 4em;
  display: flex;
  border-radius: var(--height);
  background-color: var(--primary-color);
  height: var(--height);
}

.SearchBox:hover .SearchBox-input {
  padding-left: 2em;
  padding-right: 1em;
  width: 240px;
}

.SearchBox-input {
  width: 0;
  font-size: 1.2em;
  color: #fff;
  transition: 0.45s;
}

.SearchBox-button {
  display: flex;
  border-radius: 50%;
  width: var(--height);
  height: var(--height);
  background-color: var(--accent-color);
  transition: 0.3s;
}

.SearchBox-button:active {
  transform: scale(0.85);
}

.SearchBox-icon {
  margin: auto;
  color: #fff;
}

@media screen and (min-width: 400px) {
  .SearchBox:hover .SearchBox-input {
    width: 500px;
  }
}
.pagination-wrapper .page-item:first-child .page-link {
  border-top-left-radius: 50%;
  border-bottom-left-radius: 50%;
}

.pagination-wrapper .page-item:last-child .page-link {
  border-top-right-radius: 50%;
  border-bottom-right-radius: 50%;
}

.pagination-wrapper .page-link {
  text-decoration: none !important;
  background-color: rgba(0, 0, 0, 0.315);
  color: white;
  border: none;
}

.pagination-wrapper .page-link:hover {
  background-color: #ce4d4d;
}

.pagination-wrapper .page-item.active .page-link {
  background-color: #ffffffaf;
}
</style>
