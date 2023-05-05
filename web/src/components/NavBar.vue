<template>
    <div class="navbar d-flex justify-content-center align-items-center p-3 gap-2">
        <router-link 
            v-for="link in navLinks" 
            :to="link.path"
            :key="link.name"
        >
            {{link.name}}
        </router-link>
    </div>
</template>
<script>
import {navigation} from './nav';
export default {
    name: 'NavBar',
    data() {
        return {
            navLinks: navigation,
        }
    }
}
</script>
<style lang="scss">
.navbar {
  background-color: white;
  border-radius: 1px 0 0 0;
  border-color: grey;
  border-style: solid;
  overflow: hidden;
  width: 101%;
}
</style>