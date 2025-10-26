import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Top',
    component: () => import('../views/TopPage.vue'),
    meta: { title: 'DPY Official' }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/ProfilePage.vue'),
    meta: { title: 'Profile - DPY Official' }
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: () => import('../views/GalleryPage.vue'),
    meta: { title: 'Gallery - DPY Official' }
  },
  {
    path: '/live',
    name: 'Live',
    component: () => import('../views/LivePage.vue'),
    meta: { title: 'Live - DPY Official' }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/ContactPage.vue'),
    meta: { title: 'Contact - DPY Official' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFoundPage.vue'),
    meta: { title: '404 Not Found - DPY Official' }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(_to, _from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// ページタイトル設定
router.beforeEach((to, _from, next) => {
  document.title = (to.meta.title as string) || 'DPY Official'
  next()
})

export default router
