<template>
  <div style="color:antiquewhite">
    <div class="row d-flex justify-content-around" >
      <div class="col-4">
        <p class="m-0 fs-5 user" @click="goDetail">{{ community.title }}</p>
      </div>
      <div class="col-4 text-center">
        <p class="m-0 fs-5 user" @click="goProfile">{{ community.userName }}</p>
      </div>
      <div class="col-4 text-center">
        {{ community?.created_at }}
      </div>
    </div>
    <hr>
    <!-- <div style="height:200px;"></div> -->
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    community: Object,
  },
  methods: {
    goProfile() {
      this.$router.push({ name: 'Profile', params: { user_pk: this.community.user }})
    },
    goDetail() {
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: this.community.id } })
    },
  }
}
</script>

<style>
th, td {
  text-align: left;
}
</style>