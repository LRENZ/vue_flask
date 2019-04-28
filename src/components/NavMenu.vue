<template>
  <div>
    <el-header>
      <el-menu :default-active="$route.path" router class="el-menu-demo" mode="horizontal" @select="handleSelect"
  active-text-color="#ffd04b">
        <el-menu-item index="/">Index</el-menu-item>
        <el-menu-item index="/login">Login</el-menu-item>
        <el-menu-item index="/register">Register</el-menu-item>
      </el-menu>
      <div class="line"></div>
    </el-header>
</div>
</template>
<script>
export default {
  data() {
    return {
      activeIndex: "1"
    };
  },
  methods: {
  handleSelect(key, keyPath) {
    console.log(key, keyPath);
  }
}
};
</script>
