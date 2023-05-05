<template>
    <div class="navbar d-flex justify-content-start align-items-center p-3 gap-2">
        <button
            v-for="link in navLinks" 
            @click="navigate(link.path)"
            :key="link.name"
            class="nav-btn"
        >
            {{link.name.toUpperCase()}}
        </button>
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
    },
    methods: {
        navigate(path) {
            this.$router.push({path: path})
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
.nav-btn {
    border: 0;
    background-color: white;
    font-weight: bold;

    &:hover {
        opacity: 50%;
    }
}
</style>