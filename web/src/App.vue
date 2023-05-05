<template>
  <div>
    <div>
      <NavBar/>
    </div>
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
  },
}
</script>

<style lang="scss">
.navbar {
  background-color: white;
  border-radius: 1px 0 0 0;
  border-color: grey;
  border-style: solid;
  position: fixed;
  overflow: hidden;
  width: 101%;
}
</style>
