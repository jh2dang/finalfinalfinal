import Vue from "vue";
import VueRouter from "vue-router";

import HomeView from "@/views/home/HomeView";
import MovieView from "@/views/movie/MovieView";
import MovieDetailView from "@/components/MovieDetailView";
import ReviewForm from "@/components/review/ReviewForm";
import ReviewDetail from "@/components/review/ReviewDetail";
import ReviewUpdate from "@/components/review/ReviewUpdate";

import CommunityView from "@/views/community/CommunityView";
import CommunityDetail from "@/components/community/CommunityDetail";
import CommunityFormView from "@/components/community/CommunityFormView";
import CommunityUpdate from "@/components/community/CommunityUpdate";

import MyProfile from "@/views/accounts/MyProfile";
import ProfileView from "@/views/accounts/ProfileView";
import LoginView from "@/views/accounts/LoginView";
import SignupView from "@/views/accounts/SignupView";

import NotFound404 from "@/views/NotFound404";

import OttView from "@/views/movie/OttView";
import NetflixItem from "@/components/NetflixItem";
import TvingItem from "@/components/TvingItem";
import WatchaItem from "@/components/WatchaItem";
import WavveItem from "@/components/WavveItem";
import DisneyItem from "@/components/DisneyItem";

import CinemaNow from "@/components/CinemaNow";
import CinemaUpcoming from "@/components/CinemaUpcoming";
// import UpdateDate from '@/components/UpdateDate'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "index",
    component: HomeView,
  },
  {
    path: "/home",
    name: "index",
    component: HomeView,
  },
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/movie/",
    name: "Movie",
    component: MovieView,
  },
  {
    path: "/community",
    name: "Community",
    component: CommunityView,
  },
  {
    path: "/community/:community_pk",
    name: "CommunityDetail",
    component: CommunityDetail,
  },
  {
    path: "/community/create",
    name: "CommunityCreate",
    component: CommunityFormView,
  },
  {
    path: "/community/update/:community_pk",
    name: "CommunityUpdate",
    component: CommunityUpdate,
  },
  {
    path: "/profile/",
    name: "MyProfile",
    component: MyProfile,
  },
  {
    path: "/profile/:user_pk",
    name: "Profile",
    component: ProfileView,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/signup",
    name: "Signup",
    component: SignupView,
  },
  {
    path: "/:movie_id",
    name: "MovieDetail",
    component: MovieDetailView,
  },
  {
    path: "/:movie_id/review/create",
    name: "ReviewForm",
    component: ReviewForm,
  },
  {
    path: "/:movie_id/review/:review_pk",
    name: "ReviewDetail",
    component: ReviewDetail,
  },
  {
    path: "/:movie_id/review/:review_pk/update",
    name: "ReviewUpdate",
    component: ReviewUpdate,
  },
  {
    path: "/movies/api/ott",
    name: "OttView",
    component: OttView,
    children: [
      {
        path: "",
        name: "OttViewHome",
        component: NetflixItem,
      },
      {
        path: "/movies/api/ott",
        name: "NetflixItem",
        component: NetflixItem,
      },
      {
        path: "/movies/api/ott/?page=2",
        name: "TvingItem",
        component: TvingItem,
      },
      {
        path: "/movies/api/ott/?page=3",
        name: "WatchaItem",
        component: WatchaItem,
      },
      {
        path: "/movies/api/ott/?page=4",
        name: "WavveItem",
        component: WavveItem,
      },
      {
        path: "/movies/api/ott/?page=5",
        name: "DisneyItem",
        component: DisneyItem,
      },
    ],
  },
  {
    path: "/movies/cinemanow",
    name: "CinemaNow",
    component: CinemaNow,
  },
  {
    path: "/movies/cinemaupcoming",
    name: "CinemaUpcoming",
    component: CinemaUpcoming,
  },

  {
    path: "/404",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  },
});

export default router;
