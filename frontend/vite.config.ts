import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: process.env.GITHUB_PAGES === 'true' ? '/dpyOfficial/' : '/',
  build: {
    outDir: process.env.GITHUB_PAGES === 'true' ? '../docs' : '../backend/app/static',
    emptyOutDir: true,
  },
})
