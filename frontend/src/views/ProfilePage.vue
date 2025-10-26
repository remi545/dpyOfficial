<script setup lang="ts">
// TODO: プロフィール情報とディスコグラフィーをAPIから取得
</script>

<template>
  <div class="text-white">
    <div class="container mx-auto px-4 py-16">
      <h1 class="text-4xl font-bold mb-8">Profile</h1>
      <div class="prose prose-invert max-w-none">
        <p class="text-lg mb-4">
          DPYのプロフィール情報とディスコグラフィーを表示します。
        </p>
        <p class="text-gray-400">
          ※ 実装予定: プロフィール詳細、ディスコグラフィー一覧、配信リンク等
        </p>
      </div>
      <div class="mt-8">
        <router-link to="/" class="text-blue-400 hover:text-blue-300">
          ← トップページに戻る
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
