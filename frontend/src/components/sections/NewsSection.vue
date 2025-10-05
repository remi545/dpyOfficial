<template>
  <section class="relative z-10 py-24 px-6">
    <div class="container mx-auto">
      <!-- セクションタイトル -->
      <div class="text-center mb-12">
        <div class="text-red-400 text-sm font-medium tracking-[0.3em] uppercase mb-4">What's New</div>
        <h2 class="text-5xl md:text-6xl font-bold text-white mb-6">Latest News</h2>
        <div class="w-20 h-1 bg-gradient-to-r from-red-500 to-rose-500 mx-auto rounded-full"></div>
      </div>
      
      <!-- ニュースグリッド -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <NewsCard 
          v-for="news in newsItems" 
          :key="news.id"
          :news="news"
        />
      </div>
      
      <!-- もっと見るボタン -->
      <div class="text-center mt-16">
        <a href="#news" class="group inline-flex items-center text-white/60 hover:text-white text-lg font-medium transition-all duration-300 hover:scale-105">
          <span>すべてのニュースを見る</span>
          <svg class="w-4 h-4 min-w-4 min-h-4 max-w-4 max-h-4 ml-3 flex-shrink-0 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
          </svg>
        </a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import NewsCard from '../cards/NewsCard.vue'
import type { NewsItem } from '../../types/NewsItem'

const newsItems: NewsItem[] = [
  {
    id: 1,
    date: '2024.12.15',
    title: '新曲「Aurora」リリース決定',
    content: '待望の新曲「Aurora」が12月25日にリリース決定。クリスマスに向けた特別な楽曲となっています。',
    color: 'red'
  },
  {
    id: 2,
    date: '2024.12.10',
    title: '東京ライブ開催決定',
    content: '2025年2月14日、東京・渋谷にてソロライブ開催が決定しました。チケット情報は後日発表予定です。',
    color: 'rose'
  },
  {
    id: 3,
    date: '2024.12.01',
    title: '新しいギターを導入',
    content: 'レコーディング用に新しいギターを導入しました。今後の楽曲制作にご期待ください。',
    color: 'orange'
  }
]
</script>