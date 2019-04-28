<template>
<div class="demo-image">
  <div class="block" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
    <el-image
      style="max-width: 1000px; max-height: 1000px"
      :src="url"
      :fit="fit"></el-image>
  </div>
</div>
</template>

<script>
  export default {
    name:'test',
    data() {
      return {
        fits: ['fill', 'contain', 'cover', 'none', 'scale-down'],
        url: 'https://linpiner.com/admin/image/api/file/?id=5b5699ed22382843ec83cf18&coll=images'
      }
    },
    created(){

    }
  }
</script>
