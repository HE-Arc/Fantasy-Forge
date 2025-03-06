<script setup>
import { ref, watchEffect } from "vue";
import { useRouter } from "vue-router";
import { logout } from "../../auth.js";
import IconLogout from "../icons/IconLogout.vue";

const router = useRouter();
const errorMessage = ref("");
const isAuthenticated = ref(!!localStorage.getItem("access"));

// Watch for changes to localStorage and update isAuthenticated
watchEffect(() => {
  isAuthenticated.value = !!localStorage.getItem("access");
});

async function handleLogout() {
  try {
    await logout();
    localStorage.removeItem("access");
    isAuthenticated.value = false;
    router.push("/login");
  } catch (error) {
    errorMessage.value = "Error logging out.";
  }
}
</script>

<template>
  <div v-if="isAuthenticated">
    <router-link to="#" @click.prevent="handleLogout" class="text-gray-400 dark:text-white-400 inline-block py-2 px-4 text-sm font-medium">
      <IconLogout class="inline-block" />
      Logout
    </router-link>
  </div>
  <div v-else>
    <router-link :to="{ name: 'login' }" class="text-gray-400 dark:text-white-400 inline-block py-2 px-4 text-sm font-medium">
      <IconLogin class="inline-block" />
      Login
    </router-link>
  </div>
</template>
