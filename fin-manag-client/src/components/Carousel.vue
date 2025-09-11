<script setup lang="ts">

</script>

<template>
    <section class="px-10 py-10 bg-yellow-100">
        <div class="flex flex-row w-full">
            <!-- 
                1. Need to hide overflow. 
                2. Need to dynamically add the list of things to display. 
                3. Need to add left right scroll buttons.  
            -->
            <div class="w-64 h-auto bg-gray-500"></div>
            <p class="text">This is my text 1</p>
            <p class="text">This is my text 2</p>
            <p class="text">This is my text 3</p>
            <p class="text">This is my text 4</p>
            <p class="text">This is my text 5</p>
            <p class="text">This is my text 6</p>
            <p class="text">This is my text 7</p>
            <div class="w-64 h-auto bg-gray-500"></div>
        </div>
    </section>
</template>

<style scoped>
    .text {
        margin-left: 0.25rem;
        margin-right: 0.25rem;
        font-size: 1rem;
        font-weight: bold;
        color: blue;
        background-color: red;
        flex-grow: 1;
    }
</style>