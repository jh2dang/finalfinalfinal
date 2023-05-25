<template>

<div style="width:1800px;">

  <div v-if="ottData" style="margin-top:100px; margin-left:30px;">
    <div id="title" class="title">WAVVE CHART</div>
    <hr>
    <div class="d-flex mt-3 ml-3">
      <div style="width:33%">
        <div
          v-for="(ott, index) in ottData" :key="index"
          class="rounded d-flex mb-2 align-items-center"
          @mouseover="showLargeImage(ott.poster_url, ott.rank)"
          >
          <h1 class="fw-bold ml-1 mr-2">{{ ott.rank }}</h1>
          <img :src="ott.poster_url" :alt="ott.title" class="custom-img-size mx-2"/>
          <h5>{{ ott.title }}</h5>
        </div>
      </div>
      <div class="border border-danger" style="width:45%; position: fixed; left: 50%;" v-if="showingLargeImage">
        <div class="d-flex">
          <img :src="largeImageUrl" class="large-img-size" />
          <div class="d-flex flex-column">
            <div class="d-flex">
              <p class="big fs-bold mx-3">{{ largeRank }}</p>
              <div class="mt-3">
                <p class="fs-4 text">지금 Wavve에서</p>
                <p class="fs-1 text">번째로</p>
                <p class="fs-4 text">인기 많은 영화에요.</p>
              </div>
            </div>
            <div class="ml-5">
              <button class="btn btn-outline-danger"><img src="@/assets/wavve.png" alt="logo" class="mr-2" style="width:24px; height:24px;">Wavve로 보러가기 ></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WavveItem',
  data() {
    return {
      ottData: [],
      showingLargeImage: false,
      largeImageUrl: '',
      largeRank: '',
    };
  },
  created() {
    this.fetchOttData();
  },
  methods: {
    async fetchOttData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/movies/api/ott/?page=3');
        console.log(response.data.results);
        this.ottData = response.data.results;
      } catch (error) {
        console.error(error);
      }
    },
    showLargeImage(url, rank) {
      this.showingLargeImage = true;
      this.largeImageUrl = url;
      this.largeRank = rank;
    },
    // hideLargeImage() {
    //   this.showingLargeImage = false;
    //   this.largeImageUrl = '';
    // },
  },
};
</script>


<style>

@font-face {
    font-family: 'SEBANG_Gothic_Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/SEBANG_Gothic_Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}


@font-face {
    font-family: 'GangwonEduPowerExtraBoldA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEduPowerExtraBoldA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

#title {
  font-family: 'SEBANG_Gothic_Bold';
  text-shadow: 1px 1px 6px black;
  font-size: 3rem;
}
/* 투명도 조절 */
.rounded {
  background-color: rgba(0, 0, 0, 0.315);
}

.vertical-line {
  width: 1px;
  background-color: rgba(255, 255, 255, 0.87);
  margin: 0 10px;
}

.custom-img-size {
  width: 30px;
  height: 50px;
}

.large-img-size {
  width: 400px;
  height: 600px;
}

.big {
  font-family: 'GangwonEduPowerExtraBoldA';
  font-size: 10rem;
}

.text {
  margin-bottom: -0.25rem !important;
}

/* .title {
  font-family: 'SEBANG_Gothic_Bold';
  text-shadow: 6px 6px 6px black;
} */
</style>