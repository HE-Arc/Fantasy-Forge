<script setup>
import { ref } from 'vue';
import LoginLogout from '@/components/functional/LoginLogout.vue';
import IconCharacter from './icons/IconCharacter.vue';
import IconRules from './icons/IconRules.vue';
import IconAbout from './icons/IconAbout.vue';
import IconMobileMenu from './icons/IconMobileMenu.vue';

// State for mobile menu toggle
const isMenuOpen = ref(false);
</script>

<template>
  <div class="bg-gray-100 text-white">
    <div class="bg-white dark:bg-gray-800 border-b border-gray-100 dark:border-gray-700 w-full">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo (Left) -->
          <div class="flex-shrink-0">
            <img src="@/assets/logo-app.svg" alt="App Logo" class="h-8 w-auto block dark:hidden" />
            <img src="@/assets/logo-app-dark.svg" alt="App Logo Dark" class="h-8 w-auto hidden dark:block" />
          </div>

          <!-- Desktop Navigation (Centered) -->
          <div class="hidden md:flex flex-1 justify-center">
            <ul class="flex space-x-8">
              <li>
                <router-link :to="{ name: 'characters' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
                  <IconCharacter class="inline-block" />
                  Characters
                </router-link>
              </li>
              <li>
                <router-link :to="{ name: 'rules', params: {name: ''} }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
                  <IconRules class="inline-block" />
                  Rules
                </router-link>
              </li>
              <li>
                <router-link :to="{ name: 'about' }" class="text-gray-900 dark:text-gray-100 inline-block py-2 px-4 text-sm font-medium">
                  <IconAbout class="inline-block" />
                  About
                </router-link>
              </li>
            </ul>
          </div>

          <!-- LoginLogout (Always Right) -->
          <div class="hidden md:block">
            <LoginLogout />
          </div>

          <!-- Mobile Menu Button (Right) -->
          <button class="md:hidden text-gray-900 dark:text-gray-100 focus:outline-none" @click="isMenuOpen = !isMenuOpen">
            <IconMobileMenu />
          </button>
        </div>

        <!-- Mobile Menu (Hidden by Default) -->
        <div v-if="isMenuOpen" class="md:hidden mt-2 space-y-2 bg-white dark:bg-gray-800 p-4 rounded-lg">
          <router-link :to="{ name: 'characters' }" class="block text-gray-900 dark:text-gray-100 py-2 px-4 text-sm font-medium" @click="isMenuOpen = false">
            <IconCharacter class="inline-block" />
            Characters
          </router-link>
          <router-link :to="{ name: 'rules', params: {name: ''} }" class="block text-gray-900 dark:text-gray-100 py-2 px-4 text-sm font-medium" @click="isMenuOpen = false">
            <IconRules class="inline-block" />
            Rules
          </router-link>
          <router-link :to="{ name: 'about' }" class="block text-gray-900 dark:text-gray-100 py-2 px-4 text-sm font-medium" @click="isMenuOpen = false">
            <IconAbout class="inline-block" />
            About
          </router-link>
          <LoginLogout :updateMenuState="(state) => isMenuOpen = state" />
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped></style>
