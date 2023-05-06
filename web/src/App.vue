<template>
  <div class="body">
    <div class="border-bottom">
      <NavBar/>
    </div>
    <div class="container mt-3">
      <transition name="slide-fade">
        <router-view />
      </transition>
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
body {
  background-color: #363636;
  color: white;
}
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
