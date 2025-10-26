import { defineConfig } from 'vite'
import type { Plugin } from 'vite'
import vue from '@vitejs/plugin-vue'

// index.htmlのプレースホルダーを置換するプラグイン
function htmlReplace(): Plugin {
  const isGitHubPages = process.env.GITHUB_PAGES === 'true'
  const baseUrl = isGitHubPages 
    ? 'https://remi545.github.io/dpyOfficial' 
    : 'http://localhost:8000'

  return {
    name: 'html-replace',
    transformIndexHtml(html) {
      return html.replace(/\{\{BASE_URL\}\}/g, baseUrl)
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), htmlReplace()],
  base: process.env.GITHUB_PAGES === 'true' ? '/dpyOfficial/' : '/',
  build: {
    outDir: process.env.GITHUB_PAGES === 'true' ? '../docs' : '../backend/app/static',
    emptyOutDir: true,
  },
})
