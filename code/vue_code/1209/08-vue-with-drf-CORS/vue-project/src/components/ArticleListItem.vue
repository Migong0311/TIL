<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>title: {{ article.title }}</p>
    <p>content: {{ article.content }}</p>
    <!--<RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      [DETAIL]
    </RouterLink> -->

    <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">
      Detail
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
// import { RouterLink } from 'vue-router'
import DetailView from '@/views/DetailView.vue';
import { RouterLink } from 'vue-router';
defineProps({
  article: Object,
})
</script>
