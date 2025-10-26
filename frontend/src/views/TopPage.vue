<template>
  <div class="overflow-hidden">
    <!-- メインビジュアル -->
    <HeroSection />

    <!-- 最新ニュース -->
    <NewsSection />

    <!-- SNSリンク -->
    <SocialSection />

  <!-- フッター -->
  </div>
</template>

<script setup lang="ts">
// ...existing code...
import HeroSection from '../components/sections/HeroSection.vue'
import NewsSection from '../components/sections/NewsSection.vue'
import SocialSection from '../components/sections/SocialSection.vue'

</script>