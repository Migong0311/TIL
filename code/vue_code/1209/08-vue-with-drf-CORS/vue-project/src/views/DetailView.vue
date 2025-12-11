<template>
  <div>
    <h1>Detail</h1>
    <div>
      <!-- 옵셔널 체이닝 방식으로 null 방지 -->
      <p>글 번호: {{ article?.id }}</p>
      <p>제목: {{ article?.title }}</p>
      <p>내용: {{ article?.content }}</p>
      <p>작성시간: {{ article?.created_at }}</p>
      <p>수정시간: {{ article?.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const route = useRoute()
// 단일 조회 시 배열로조회를 하면 복수의 데이터를 조회 할 떄 이기 떄문에 null로 선언해줘야함
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then(res => {
      console.log(res.data)
      article.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style></style>
