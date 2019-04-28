<template>
  <div id="app">
    <el-main>
      <el-row :gutter="14" type="flex">
      <NavMenu></NavMenu>
    </el-row>
    <router-view/>
    </el-main>
  </div>
</template>

<script>
import NavMenu from "./components/NavMenu";
export default{
  name: 'App',
  components:{
      'NavMenu':NavMenu
  },
}
</script>
