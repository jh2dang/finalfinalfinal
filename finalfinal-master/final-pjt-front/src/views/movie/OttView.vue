<template>
  <div class="bg-dark text-white mt-4">
    <div class="px-2">
      <!-- <router-link
        :to="{ name: 'NetflixItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button1"
      > -->
      <router-link
        :to="{ name: 'NetflixItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button1"
      >
        <img src="@/assets/netflix.png" alt="logo" class="mr-2" />
        Netflix
      </router-link>
      <router-link
        :to="{ name: 'TvingItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button2"
      >
        <img
          src="@/assets/tving.png"
          alt="logo"
          class="mr-2 rounded"
          style="width: 24px; height: 24px"
        />
        Tving
      </router-link>
      <router-link
        :to="{ name: 'WatchaItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button3"
      >
        <img
          src="@/assets/watcha.png"
          alt="logo"
          class="mr-2"
          style="width: 24px; height: 24px"
        />
        Watcha
      </router-link>
      <router-link
        :to="{ name: 'WavveItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button4"
      >
        <img
          src="@/assets/wavve.png"
          alt="logo"
          class="mr-2 rounded"
          style="width: 24px; height: 24px"
        />
        Wavve
      </router-link>
      <router-link
        :to="{ name: 'DisneyItem' }"
        class="btn btn-outline-light mx-2 animated-button animated-button5"
      >
        <img
          src="@/assets/disney.png"
          alt="logo"
          class="mr-2"
          style="width: 24px; height: 24px"
        />
        Disney
      </router-link>
    </div>

    <!-- <NetflixItem /> -->
    <router-view />
    <p>보고싶은 ott 페이지를 눌러주세요</p>
  </div>
</template>

<script>
export default {
  name: "OttView",
};
</script>

<style>

.custom-btn {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}

.btn-8 {
  background-color: #f0ecfc;
background-image: linear-gradient(315deg, #f0ecfc 0%, #c797eb 74%);
  line-height: 42px;
  padding: 0;
  border: none;
}
.btn-8 span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.btn-8:before,
.btn-8:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  background: #c797eb;
  /*box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);*/
  transition: all 0.3s ease;
}
.btn-8:before{
   height: 0%;
   width: 2px;
}
.btn-8:after {
  width: 0%;
  height: 2px;
}
.btn-8:hover:before {
  height: 100%;
}
.btn-8:hover:after {
  width: 100%;
}
.btn-8:hover{
  background: transparent;
}
.btn-8 span:hover{
  color: #c797eb;
}
.btn-8 span:before,
.btn-8 span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  background: #c797eb;
  /*box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);*/
  transition: all 0.3s ease;
}
.btn-8 span:before {
  width: 2px;
  height: 0%;
}
.btn-8 span:after {
  height: 2px;
  width: 0%;
}
.btn-8 span:hover:before {
  height: 100%;
}
.btn-8 span:hover:after {
  width: 100%;
}
  



.animated-button {
  position: relative;
  overflow: hidden;
}

.animated-button::before,
.animated-button::after {
  content: "";
  position: absolute;
  width: 0;
  height: 2px;
  left: 50%;
  bottom: 0;
  background-color: #000;
  transition: width 0.3s ease;
}

.animated-button::before {
  transform: translateX(-50%);
  transform-origin: right;
}

.animated-button::after {
  transform: translateX(-50%);
  transform-origin: left;
}

.animated-button:hover::before,
.animated-button:hover::after {
  width: 100%;
}

/* 다른 애니메이션 스타일 */
.animated-button1::before,
.animated-button1::after {
  background-color: #ff0000;
}

.animated-button2::before,
.animated-button2::after {
  background-color: #00ff00;
}

.animated-button3::before,
.animated-button3::after {
  background-color: #0000ff;
}

.animated-button4::before,
.animated-button4::after {
  background-color: #ffff00;
}

.animated-button5::before,
.animated-button5::after {
  background-color: #ff00ff;
}
</style>
