<template>
    <div>
        <ParentChild 
        @some-event="someCallback" 
        my-msg="love message" 
        @emit-args="getNumbers"
        @update-name="updateName" />
    </div>
    <hr>
    <div>
        <ParentItem 
        v-for="item in items" 
        :key="item.id" 
        :my-prob="item" />
    </div>
    <hr>
    <p>{{ name }}</p>
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from './ParentChild.vue';
import ParentItem from './ParentItem.vue';

const items = ref([
    { id: 1, name: 'apple' },
    { id: 2, name: 'banana' },
    { id: 3, name: 'strawbarry' },
])

const someCallback = () => {
    console.log('ParentChild가 발신한 이벤트를 수신했어요')
}

const getNumbers = (...args) => {
    console.log(args)
    console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요`)
}

const name = ref('Alice')

const updateName = () => {
    name.value = 'Bella'
}
</script>

<style scoped></style>