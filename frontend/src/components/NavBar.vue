<script setup>
import { ref } from 'vue'
</script>

<template>
  <div class="bg-gray-100 text-white">
    <!-- Navigation Tabs -->
    <div class="bg-white dark:bg-gray-800 border-b border-gray-100 dark:border-gray-700 w-full">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <ul class="flex justify-center items-center space-x-8 h-full">
          <li>
                <img src="@/assets/logo-app.svg" alt="App Logo" class="h-12 w-auto block dark:hidden" />
                <img src="@/assets/logo-app-dark.svg" alt="App Logo Dark" class="h-12 w-auto hidden dark:block" />
          </li>
          <li>
            <router-link :to="{ name: 'characters' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
              <img src="https://seiyria.com/gameicons-font/svg/warlord-helmet.svg" alt="Characters" class="h-6 w-auto inline-block" />
              Characters
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'classes' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
              <img src="https://seiyria.com/gameicons-font/svg/bookshelf.svg" alt="Rules" class="h-6 w-auto inline-block" />
              Rules
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'about' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
              <img src="https://seiyria.com/gameicons-font/svg/scroll-unfurled.svg" alt="About" class="h-6 w-auto inline-block" />
              About
            </router-link>
          </li>
          <li>
            <!-- TODO if logged in - log out -->
            <router-link :to="{ name: 'login' }" class="text-gray-400 dark:text-white-400 inline-block py-2 px-4 text-sm font-medium">
              <img src="https://seiyria.com/gameicons-font/svg/entry-door.svg" alt="Login" class="h-6 w-auto inline-block" />
              Login
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
