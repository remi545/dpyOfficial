<template>
  <section class="relative z-10 min-h-screen flex items-center justify-center px-6">
    <div class="container mx-auto text-center">
      <div class="space-y-8">
        <!-- サブタイトル -->
        <div class="text-red-400 text-sm font-medium tracking-[0.3em] uppercase">
          Guitarist • Composer • Producer
        </div>

        <!-- メインタイトル -->
        <h1 class="text-7xl md:text-9xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-red-100 tracking-tight leading-none">
          DPY
        </h1>

        <!-- 装飾ライン -->
        <div class="flex items-center justify-center space-x-2">
          <div class="w-16 h-px bg-gradient-to-r from-transparent to-red-400"></div>
        </div>

        <!-- キャッチフレーズ -->
        <p class="text-xl md:text-2xl text-white/70 max-w-3xl mx-auto leading-relaxed">
          音楽の境界を超え、感情を形にする。<br class="hidden md:block">
          革新的なサウンドで新たな体験を創造する。
        </p>

        <!-- CTA ボタン -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-6 pt-8">
          <button class="bg-gradient-to-r from-red-600 to-rose-600 text-white px-10 py-4 rounded-full font-semibold text-lg shadow-lg hover:scale-105 transition-all duration-200">
            最新楽曲を聴く
          </button>
          <button class="border-2 border-white/20 text-white hover:border-white/40 px-10 py-4 rounded-full font-semibold text-lg transition-all duration-200 hover:scale-105">
            プロフィール
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
// ヒーローセクション用コンポーネント
</script>