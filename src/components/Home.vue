<template>
  <div id="app">
        <el-row :gutter="14" type="flex" justify='center'>
         <el-col :xs="16" :sm="16" :md="16" :lg="8" :xl="8" offset="3">
           <div class="grid-content bg-purple">
           </br>
      <el-image
        style="max-width: 300px; max-height: 300px"
        src="https://linpiner.com/admin/image/api/file/?id=5b5699ed22382843ec83cf18&coll=images"
        fit="contain"></el-image>
        <p>欢迎，{{user ? user.username : "游客"}}</p>
           <el-button @click="test">test</el-button>
           <el-button @click="startHacking" v-if="user">Start</el-button>
           <el-button @click="login" v-else>去登录</el-button>
           <el-button @click="logout" v-if="user">登出</el-button>
         </div>
         </el-col>
        </el-row>

        <el-row justify='center'>
          <el-col>
          <el-carousel :interval="5000" type="card" indicator-position="none">
                 <el-carousel-item v-for="item in URL" :key="item" >
                   <el-image :src="item" fit="contain" style="height:100%">
                   </el-image>
                 </el-carousel-item>
           </el-carousel>
         </el-col>

        </el-row>

        <el-row>
          <el-col :span="24" :xs="18" :sm="18" :md="18" :lg="10" :xl="6" v-for="(o, index) in 8" :key="o" :offset="4" style="margin-bottom:40px">
            <el-card :body-style="{ padding: '0px' }">
              <el-image src="https://linpiner.com/admin/image/api/file/?id=5b5699ed22382843ec83cf18&coll=images" class="image" fit="contain">
              </el-image>
              <div style="padding: 14px;">
                <span>好吃的汉堡</span>
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button">操作按钮</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
    </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  components:{

  },
  data() {
  return {
    currentDate: new Date(),
    URL:[
      "https://linpiner.com/admin/image/api/file/?id=5b90817722382842b8aef11c&coll=images",
      "https://linpiner.com/admin/image/api/file/?id=5b7fbcfa22382817a9889dd3&coll=images",
      "https://linpiner.com/admin/image/api/file/?id=5b5699ed22382843ec83cf18&coll=images",
      "https://linpiner.com/admin/image/api/file/?id=5b55ecd12238282f2cbef131&coll=images",
      "https://linpiner.com/admin/image/api/file/?id=5b55ec852238282f2d2008d2&coll=images",
    ]
  };
  },
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
    },
    test() {
      this.$router.push('/test')
    },

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
 {
  text-align: center;
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}




.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}


</style>
