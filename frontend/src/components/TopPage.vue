<template>
  <div class="min-h-screen bg-black overflow-hidden">
  <!-- 背景アニメーション削除 -->

    <!-- ヘッダー -->
    <Header />
    
    <!-- メインビジュアル -->
    <HeroSection />

    <!-- 最新ニュース -->
    <NewsSection />

    <!-- SNSリンク -->
    <SocialSection />

    <!-- フッター -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
// ...existing code...
import Header from './layout/Header.vue'
import HeroSection from './sections/HeroSection.vue'
import NewsSection from './sections/NewsSection.vue'
import SocialSection from './sections/SocialSection.vue'
import Footer from './layout/Footer.vue'
</script>