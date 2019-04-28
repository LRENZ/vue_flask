<template>
  <div>
    <div class="container">
    <el-main>
    <el-row :gutter="14" type="flex" justify='center' align='middle'>
     <el-col :xs="20" :sm="20" :md="20" :lg="8" :xl="8" >
       <div class="grid-content bg-purple">
         <h1>Hello, Login</h1>
        <el-form :model="loginFormFields" ref="loginForm" :rules="rules" v-loading="loading" label-position='top' style="margin: 20px">
          <el-form-item label="User Name" prop="username">
            <el-input v-model="loginFormFields.username"></el-input>
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input v-model="loginFormFields.password" type="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('loginForm')">Login</el-button>
          </el-form-item>
        </el-form>
        <p>New User？<router-link to="/register">Register</router-link></p>
        </div>
     </el-col>
    </el-row>
  </el-main>
  </div>
</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "LoginForm",
  data() {
    return {
      loginFormFields: {
        username: "",
        password: ""
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" }
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$store.dispatch("login", this.loginFormFields).then(() => {
            if (this.error) {
              this.$message.error(this.error);
            } else {
              this.$message.success("登录成功！");
              this.$router.push('/')
            }
          });
        } else {
          return false;
        }
      });
    }
  },
  computed: {
    ...mapGetters(["loading", "error"])
  }
};
</script>

<style scoped>
 h1 {
  text-align: center;
}
</style>
