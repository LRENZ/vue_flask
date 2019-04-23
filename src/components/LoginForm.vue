<template>
  <div>
    <h1>登录</h1>
    <el-form :model="loginFormFields" ref="loginForm" label-width="80px" :rules="rules" v-loading="loading">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="loginFormFields.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="loginFormFields.password" type="password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
      </el-form-item>
    </el-form>
    <p>新用户？<router-link to="/register">点此注册</router-link></p>
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
* {
  text-align: center;
}
</style>
