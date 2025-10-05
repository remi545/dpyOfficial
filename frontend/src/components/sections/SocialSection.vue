<template>
  <section class="relative z-10 py-24 px-6">
    <div class="container mx-auto">
      <!-- セクションタイトル -->
      <div class="text-center mb-16">
        <div class="text-violet-400 text-sm font-medium tracking-[0.3em] uppercase mb-4">Connect</div>
        <h2 class="text-5xl md:text-6xl font-bold text-white mb-6">Follow Me</h2>
        <div class="w-24 h-1 bg-gradient-to-r from-violet-500 to-fuchsia-500 mx-auto rounded-full"></div>
      </div>
      
      <!-- SNSリンク -->
      <div class="flex justify-center items-center space-x-12">
        <SocialLink 
          v-for="social in socialLinks" 
          :key="social.name"
          :social="social"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import SocialLink from '../links/SocialLink.vue'
import type { SocialItem } from '../../types/SocialItem'

const socialLinks: SocialItem[] = [
  {
    name: 'YouTube',
    href: '#',
    color: 'red',
    gradient: 'from-red-500 to-red-600',
    icon: 'youtube'
  },
  {
    name: 'Instagram',
    href: '#',
    color: 'purple',
    gradient: 'from-purple-500 via-pink-500 to-orange-500',
    icon: 'instagram'
  },
  {
    name: 'X',
    href: '#',
    color: 'gray',
    gradient: 'from-gray-800 to-black',
    icon: 'x'
  },
  {
    name: 'Spotify',
    href: '#',
    color: 'green',
    gradient: 'from-green-500 to-green-600',
    icon: 'spotify'
  }
]
</script>