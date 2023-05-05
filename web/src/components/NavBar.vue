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
    },
    mounted() {
        console.log(this.navLinks);
    }
}
</script>