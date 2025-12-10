<template>
  <h1>{{ store.count }}</h1>
  <h3>{{ store.doubleCount }}</h3>
  <button @click="store.increment">+++</button>
</template>

<script setup>
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

store.increment()
console.log(store.count)
console.log(store.doubleCount)
  const newNumber = store.count + 1
</script>

<style scoped></style>
