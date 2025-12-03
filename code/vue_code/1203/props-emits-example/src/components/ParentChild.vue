<template>
    <div>
        <h3>ParentChild</h3>
        <p>Parent Message : {{ myMsg }}</p>
        <ParentGrandChild :my-msg="myMsg" @update-name="updateName"/>
    </div>
    <!-- <button @click="$emit('someEvent')">click</button> -->
    <button @click="buttonClick">buttonClick!! </button>
    <div>
        <button @click="emitArgs">추가 인자 전달</button>
    </div>
</template>

<script setup>
import ParentGrandChild from './ParentGrandChild.vue';

defineProps({
    myMsg: String
})
const emit = defineEmits([
    'someEvent','emitArgs','updateName'
])
const buttonClick = () => {
    emit('someEvent')
}

const emitArgs = () => {
    emit('emitArgs', 1, 2, 3)
}

const updateName = ()=>{
    emit('updateName')
}

</script>


<style scoped></style>
