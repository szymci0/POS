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
