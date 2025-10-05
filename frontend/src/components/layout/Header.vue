<template>
  <header class="fixed top-0 left-0 right-0 z-50 bg-black/10 backdrop-blur-xl border-b border-white/5">
    <nav class="container mx-auto px-6 py-4">
      <div class="flex items-center justify-between">
        <!-- ロゴ -->
        <div class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-rose-500">
          DPY
        </div>
        
        <!-- ナビゲーションメニュー -->
        <div class="hidden md:flex items-center space-x-8">
          <a 
            v-for="item in menuItems" 
            :key="item.name"
            :href="item.href" 
            class="text-white/80 hover:text-white hover:scale-105 transition-all duration-300 text-sm font-medium tracking-wide"
          >
            {{ item.name }}
          </a>
        </div>
        
        <!-- モバイルメニューボタン -->
        <button class="md:hidden text-white/80 hover:text-white transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
const menuItems = [
  { name: 'HOME', href: '#home' },
  { name: 'PROFILE', href: '#profile' },
  { name: 'GALLERY', href: '#gallery' },
  { name: 'LIVE', href: '#live' },
  { name: 'CONTACT', href: '#contact' }
]
</script>