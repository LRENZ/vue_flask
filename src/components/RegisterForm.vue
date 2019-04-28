<template>
  <div>
    <div class="container">
    <el-main>
    <el-row :gutter="14" type="flex" justify='center' align='middle'>
     <el-col :xs="20" :sm="20" :md="20" :lg="8" :xl="8" >
           <div class="grid-content bg-purple">
            <h1>Hello Register</h1>
        <el-form :model="registerFormFields" ref="registerForm" :rules="rules" v-loading="loading" label-position='top' style="margin: 20px">
          <el-form-item label="User Name" prop="username">
            <el-input v-model="registerFormFields.username"></el-input>
          </el-form-item>
          <el-form-item label="Email" prop="email">
            <el-input v-model="registerFormFields.email"></el-input>
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input v-model="registerFormFields.password" type="password" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="Confirm Password" prop="confirm">
            <el-input v-model="registerFormFields.confirm" type="password" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('registerForm')">Register Now</el-button>
          </el-form-item>
        </el-form>
        <p>Got An Account Already？<router-link to="/login">Login</router-link></p>
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
  name: "RegisterForm",
  data() {
    let validatePassword = (rule, value, cb) => {
      if (value === "") {
        cb(new Error("请输入密码"));
      } else if (this.registerFormFields.confirm !== "") {
        this.$refs.registerForm.validateField("confirm");
      }
      cb();
    };
    let validateConfirm = (rule, value, cb) => {
      if (value === "") {
        cb(new Error("请再次输入密码"));
      } else if (value !== this.registerFormFields.password) {
        cb(new Error("两次输入的密码不一致"));
      } else {
        cb();
      }
    };
    return {
      registerFormFields: {
        username: "",
        email: "",
        password: "",
        confirm: ""
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { max: 20, message: "用户名最多20个字符", trigger: "blur" }
        ],
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            type: "email",
            message: "邮箱格式不正确",
            trigger: ["blur", "change"]
          }
        ],
        password: [{ validator: validatePassword, trigger: "blur" }],
        confirm: [{ validator: validateConfirm, trigger: "blur" }]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$store.dispatch("register", this.registerFormFields).then(() => {
            if (this.error) {
              this.$message.error(this.error);
            } else {
              this.$message.success("注册成功！");
              this.$router.push('/login')
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
