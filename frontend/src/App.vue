<script setup lang="ts">
import Header from './components/layout/Header.vue'
import Footer from './components/layout/Footer.vue'
</script>

<template>
  <div id="app">
    <Header />
  <main class="pt-24 bg-gradient-to-b from-stone-950 via-stone-900 to-neutral-950 min-h-screen">
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<style scoped>
</style>
