<template>
  <div>
    <div>
      <div class="navbar d-flex justify-content-center align-items-center p-3 gap-2">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
      </div>
    </div>
    <div class="mt-5">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
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
