<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title">
      <br/>
      
      <label for="content">내용: </label>
      <textarea type="text" id="content" v-model.trim="content"></textarea>
      <br/>
      
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  // Vue 핵심 기능과 라우터, 상태 관리(Pinia), 비동기 통신 라이브러리 임포트
  import { ref } from 'vue'
  import axios from 'axios'
  import { useArticleStore } from '@/stores/articles'
  import { useRouter } from 'vue-router'

  // Pinia 스토어 인스턴스 생성 (API URL 등을 가져오기 위함)
  const store = useArticleStore()
  // 라우터 인스턴스 생성 (페이지 이동을 위함)
  const router = useRouter()

  // 반응형 변수 선언 (template의 v-model과 연결됨)
  // 초기값은 null로 설정되어 있으며, 사용자가 입력하면 그 값으로 업데이트됩니다.
  const title = ref(null)
  const content = ref(null)

  // 게시글 생성 요청 함수
  const createArticle = function () {
    // axios를 사용하여 비동기 HTTP 요청을 보냅니다.
    axios({
      // 1. HTTP Method: 자원을 생성(Create)하므로 'post' 방식을 사용합니다.
      method: 'post',
      
      // 2. URL: 서버의 게시글 생성 API 주소입니다.
      // store.API_URL은 'http://127.0.0.1:8000'과 같은 기본 도메인을 담고 있습니다.
      url: `${store.API_URL}/api/v1/articles/`,
      
      // 3. Data: 서버(DB)에 저장할 실제 데이터(Payload)입니다.
      // script 태그 내에서는 ref 변수의 값에 접근할 때 반드시 .value를 붙여야 합니다.
      data: {
        title: title.value,
        content: content.value
      }
    })        
      .then(res => {
        // 4. 성공(201 Created) 시 처리 로직
        console.log('게시글 작성 성공!')
        
        // 게시글 작성이 완료되면 사용자를 게시글 목록 페이지(ArticleView)로 이동시킵니다.
        // router.push는 <router-link>와 동일한 역할을 하는 프로그래밍 방식의 네비게이션입니다.
        router.push({ name: 'ArticleView' })
      })
      .catch(err => {
        // 5. 실패(400 Bad Request 등) 시 에러 처리 로직
        console.log(err)
      })
  }
</script>

<style>

</style>