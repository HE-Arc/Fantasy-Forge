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
            <router-link :to="{ name: 'home' }">
                <img src="@/assets/logo-app.svg" alt="App Logo" class="h-12 w-auto block dark:hidden" />
                <img src="@/assets/logo-app-dark.svg" alt="App Logo Dark" class="h-12 w-auto hidden dark:block" />
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'home' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
              Characters
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'about' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
              About
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
