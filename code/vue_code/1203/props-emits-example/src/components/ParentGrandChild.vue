<template>
    <div>
        <h4>ParentGrandChild</h4>
        <p>ParentChild Message : {{ myMsg }}</p>
    </div>
    <div><button @click="updateName">이름 변경</button></div>
</template>

<script setup>
defineProps({
    myMsg: String
})

const emit = defineEmits(['updateName'])

const updateName = ()=>{
    emit('updateName')
}

</script>
<style scoped></style>