<script setup lang="ts">
import chevronRight from "../assets/images/chevron-right.svg";
import chevronLeft from "../assets/images/chevron-left.svg";

const items: string[] = [
    'This is my text 1', 
    'This is my text 2', 
    'This is my text 3', 
    'This is my text 4', 
    'This is my text 5', 
    // 'This is my text 6', 
    // 'This is my text 7',
    // 'This is my text 8',
    // 'This is my text 9',
    // 'This is my text 10',
    // 'This is my text 11',
    // 'This is my text 12',
    // 'This is my text 13',
    // 'This is my text 14'
    ];
</script>
<!--
    - Just for a test commit. 
-->

<template>
    <section class="px-10 py-10 bg-green-700">
        <div class="flex flex-row w-full justify-center overflow-hidden">
            <button class="min-w-10 max-w-20 flex-grow bg-transparent">
                <img :src="chevronLeft" alt="left chevron" />
            </button>
            <div class="flex flex-row overflow-x-hidden mx-2">
                <span v-for="(item, index) in items" :key="index" class="text label">{{ item }}</span>
            </div>
            <button class="min-w-10 max-w-20 bg-transparent">
                <img :src="chevronRight" alt="Right chevron" />
            </button>
        </div>
    </section>
</template>

<style scoped>
    .label {
        margin-right: 0.25rem;
        padding: 0.5rem;
        border: 1px solid white;
        border-radius: 0.25rem;
        cursor: pointer;
        background-color: transparent;
    }

    .text {
        font-size: 1rem;
        color: White;
        white-space: nowrap;
    }

    .label:hover {
        background-color: black;
    }
</style>