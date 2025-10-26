<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push('/')
}
</script>

<template>
  <div class="text-white flex items-center justify-center">
    <div class="text-center">
      <h1 class="text-9xl font-bold text-gray-700 mb-4">404</h1>
      <h2 class="text-3xl font-semibold mb-6">Page Not Found</h2>
      <p class="text-gray-400 mb-8">
        お探しのページが見つかりませんでした。
      </p>
      <button
        @click="goHome"
        class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors"
      >
        トップページに戻る
      </button>
    </div>
  </div>
</template>

<style scoped>
</style>
