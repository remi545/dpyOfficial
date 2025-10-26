<script setup lang="ts">
// TODO: ライブ情報をAPIから取得
</script>

<template>
  <div class="min-h-screen bg-gray-900 text-white">
    <div class="container mx-auto px-4 py-16">
      <h1 class="text-4xl font-bold mb-8">Live</h1>
      <div class="prose prose-invert max-w-none">
        <p class="text-lg mb-4">
          DPYのライブ・イベント情報を表示します。
        </p>
        <p class="text-gray-400">
          ※ 実装予定: ライブスケジュール、会場情報、チケット情報等
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
