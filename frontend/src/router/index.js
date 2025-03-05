import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },

    {
      path: '/characters',
      name: 'characters',
      component: () => import('../views/CharactersView.vue'),
    },

    {
      path: '/characters/:id',
      name: 'character-edit',
      component: () => import('../views/CharacterEdition.vue'),
    },

    {
      path: '/characters/new',
      name: 'character-new',
      component: () => import('../views/CharacterEdition.vue'),
    },
  ],
})

export default router
