<script setup lang="ts">
  import Hero from '../components/Hero.vue';
  import HomeCards from '../components/HomeCards.vue';
  import JobListings from '../components/JobListings.vue';
  import Carousel from '../components/Carousel.vue';
</script>

<template>
    <Hero title="This is a Test Title." subtitle="This is a test sub title."/>
    <Carousel />
    <HomeCards />
    <JobListings :limit="3" :showButton="true"/>
</template>