<script setup land="ts">
  import Hero from '../components/Hero.vue';
  import HomeCards from '../components/HomeCards.vue';
  import JobListings from '../components/JobListings.vue'
</script>

<template>
    <Hero title="This is a Test Title." subtitle="This is a test sub title."/>
    <HomeCards />
    <JobListings :limit="3" :showButton="true"/>
</template>