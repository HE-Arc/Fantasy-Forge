<script setup>
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <div class="flex flex-col h-screen">
    <!-- navbar -->
    <NavBar></NavBar>
    <div class="flex-1 overflow-auto">
      <router-view />
    </div>
  </div>
</template>

<style scoped>
</style>
