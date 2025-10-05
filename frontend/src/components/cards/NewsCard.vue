<template>
  <article 
    class="group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-xl rounded-2xl p-8 border border-white/10 transition-all duration-500 hover:scale-105 hover:shadow-2xl"
    :class="cardClasses"
  >
    <div 
      class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"
      :class="backgroundClasses"
    ></div>
    <div class="relative z-10">
      <div class="flex items-center justify-between mb-4">
        <time class="text-sm font-medium" :class="textClasses">{{ news.date }}</time>
        <div class="w-2 h-2 rounded-full animate-pulse" :class="dotClasses"></div>
      </div>
      <h3 class="text-white text-xl font-bold mb-4 group-hover:transition-colors" :class="titleHoverClasses">
        {{ news.title }}
      </h3>
      <p class="text-white/60 text-sm leading-relaxed mb-6">{{ news.content }}</p>
      <div class="flex items-center text-sm font-medium group-hover:transition-colors" :class="[textClasses, titleHoverClasses]">
        <span>詳細を見る</span>
        <svg class="w-3 h-3 min-w-3 min-h-3 max-w-3 max-h-3 ml-2 flex-shrink-0 group-hover:translate-x-1 transition-transform duration-300" style="width: 12px; height: 12px;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">

import type { NewsItem } from '../../types/NewsItem'

interface Props {
  news: NewsItem
}

const props = defineProps<Props>()

const colorClasses = {
  red: {
    border: 'hover:border-red-500/30',
    shadow: 'hover:shadow-red-500/10',
    background: 'bg-gradient-to-br from-red-600/10 to-rose-600/10',
    text: 'text-red-300',
    titleHover: 'group-hover:text-red-200',
    dot: 'bg-red-400'
  },
  rose: {
    border: 'hover:border-rose-500/30',
    shadow: 'hover:shadow-rose-500/10',
    background: 'bg-gradient-to-br from-rose-600/10 to-orange-600/10',
    text: 'text-rose-300',
    titleHover: 'group-hover:text-rose-200',
    dot: 'bg-rose-400'
  },
  orange: {
    border: 'hover:border-orange-500/30',
    shadow: 'hover:shadow-orange-500/10',
    background: 'bg-gradient-to-br from-orange-600/10 to-red-600/10',
    text: 'text-orange-300',
    titleHover: 'group-hover:text-orange-200',
    dot: 'bg-orange-400'
  }
}

const cardClasses = `${colorClasses[props.news.color].border} ${colorClasses[props.news.color].shadow}`
const backgroundClasses = colorClasses[props.news.color].background
const textClasses = colorClasses[props.news.color].text
const titleHoverClasses = colorClasses[props.news.color].titleHover
const dotClasses = colorClasses[props.news.color].dot
</script>