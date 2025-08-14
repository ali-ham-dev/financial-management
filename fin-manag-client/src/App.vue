<script setup lang='ts'>
  import NavBar from './components/NavBar.vue';
  import Hero from './components/Hero.vue';
  import HomeCards from './components/HomeCards.vue';
  import JobListings from './components/JobListings.vue'
</script>

<template>
  <NavBar />
  <Hero title="This is a Test Title." subtitle="This is a test sub title."/>
  <HomeCards />
  <JobListings />
</template>