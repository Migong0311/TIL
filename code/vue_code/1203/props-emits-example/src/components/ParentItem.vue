<template>
    <h5>ParentItem</h5>
    <div>
        <p>{{ myProb.id }}</p>
        <p>{{ myProb.name }}</p>
    </div>
</template>

<script setup>
defineProps({
    myProb:Object
})
</script>

<style  scoped>

</style>