// store/articles.js

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([])

  const getArticles = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        // 데이터 확인용
        // console.log('res',res)
        // console.log('res.data',res.data)
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }
  // const articles = ref([
  //   {id:1,title:'t1',content:'c1'},
  //   {id:2,title:'t2',content:'c2'},
  // ])
  return { articles, API_URL, getArticles }
}, { persist: true })
