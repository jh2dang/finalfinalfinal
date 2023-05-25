<template>
  <div class="d-flex justify-content-center bg-dark text-white">
    <div style="width:1900px;">
        <div class="imgbox d-flex align-items-end ml-5" style="height:300px;">
            <div class="big">상영 예정작</div>
        </div>
        <div>

            <div class="cardbox d-flex flex-wrap">
                <div v-for="(movie, index) in movies" :key="index" class="card items my-2">
                    <img :src="movie.poster_url" :alt="movie.title" class="card-img-top" style="height: 270px; width: 100%;">
                    <div class="card-body text-center" style="position: relative;">
                        <h5 class="card-title">
                            <a :href="movie.info_url" target="_blank" class="text-white text-decoration-none">[ {{ movie.title }} ]</a>
                        </h5>
                        <hr>
                        <span class="smt">{{ movie.genre }} | {{ movie.runtime }}</span>
                        <br>
                        <span class="smt">개봉 | {{ movie.date }}</span>
                        <a :href="movie.reserve_url" target="_blank" class="btn btn-sm btn-danger" style="position: absolute; bottom: 15px; left:41px;">예매하러 가기 ></a>
                    </div>
                </div>
            </div>

        </div>
        <div style="height:230px;"></div>
        

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CinemaUpcoming',
    data() {
        return {
            movies: [],
        }
    },
    async created() {
        const response = await axios.get('http://127.0.0.1:8000/movies/cinemaupcoming/');
        this.movies = response.data.results;
    }
}
</script>

<style scoped>


@font-face {
    font-family: 'GangwonEduPowerExtraBoldA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEduPowerExtraBoldA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

.smt {
    color: rgba(255, 255, 255, 0.712)
}

.big {
  font-family: 'GangwonEduPowerExtraBoldA';
  font-size: 5rem;
}

.items {
    width: 180px;
    height: 500px;
    background-color: rgba(0, 0, 0, 0.315);
}

.card {
    border: none;
}

.cardbox {
    justify-content: space-evenly;
}
</style>