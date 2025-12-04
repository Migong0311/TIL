<template>
    <div>
        <RouterLink :to="{ name: 'userProfile' }">Profile</RouterLink>
        <RouterLink :to="{ name: 'userPosts' }">Posts</RouterLink>
        <h3>UserView</h3>
        <p>{{ userId }}번 유저</p>
        <button @click="goHome">홈으로!</button>
        <hr>
        <RouterView />
    </div>
</template>

<script setup>
import { RouterView, useRoute, RouterLink, useRouter,onBeforeRouteLeave } from 'vue-router';
import { ref } from 'vue';
const route = useRoute()

const router = useRouter()
const goHome = () => {
    router.push({ name: 'home' })
    // router.replace({ name: 'home' })
}
const userId = ref(route.params.id)

onBeforeRouteLeave((to,from)=>{
    const answer = window.confirm('가지마요 ㅠㅠ')
    if(answer === false){
        return false
    }
})
</script>

<style scoped></style>