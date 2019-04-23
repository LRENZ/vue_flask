<template>
  <div id="app">
    <img src="../assets/logo.png">
    <p>test，{{user ? user.username : "游客"}}</p>
    <el-button @click="startHacking" v-if="user">Start</el-button>
    <el-button @click="login" v-else>去登录</el-button>
    <el-button @click="logout" v-if="user">登出</el-button>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  methods: {
    startHacking() {
      axios.get("/api/v1").then((res) => {
        this.$notify({
          title: `当前api版本: ${res.data.api_version}`,
          type: "success",
          message:
            "We've laid the ground work for you. It's time for you to build something epic!",
          duration: 5000
        });
      });
    },
    login() {
      this.$router.push('/login')
    },
    logout() {
      this.$store.dispatch('logout')
    }
  },
  created() {
    let token = localStorage.getItem('token')
    if(token) {this.$store.dispatch('loadUser', token)}
  },
  computed: {
    ...mapGetters(['user'])
  }
};
</script>

<style scoped>
* {
  text-align: center;
}
</style>
