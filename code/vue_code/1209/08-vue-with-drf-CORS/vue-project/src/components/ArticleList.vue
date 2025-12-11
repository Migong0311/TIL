<template>
  <div>
    <h3>Article List</h3>
    <!-- <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    /> -->
    <ArticleListItem 
    v-for="article in store.articles"
    :key="article.id"
    :article="article"/>
  </div>
</template>

<script setup>
import ArticleListItem from './ArticleListItem.vue';
import { useArticleStore } from '@/stores/articles';

const store = useArticleStore()

</script>
