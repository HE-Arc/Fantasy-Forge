<script setup>
import { ref, watchEffect } from "vue";
import { useRouter } from "vue-router";
import { logout } from "../../auth.js";
import IconLogout from "../icons/IconLogout.vue";
import IconLogin from "../icons/IconLogin.vue";

const router = useRouter();
const errorMessage = ref("");
const isAuthenticated = ref(!!localStorage.getItem("access"));

// Watch for changes to localStorage and update isAuthenticated
watchEffect(() => {
  isAuthenticated.value = !!localStorage.getItem("access");
});

defineProps(["updateMenuState"]);

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
    <router-link to="#" @click.prevent="handleLogout" class="block text-gray-900 dark:text-gray-100 py-2 px-4 text-sm font-medium" @click="updateMenuState(false)">
      <IconLogout class="inline-block" />
      Logout
    </router-link>
  </div>
  <div v-else>
    <router-link :to="{ name: 'login' }" class="block text-gray-900 dark:text-gray-100 py-2 px-4 text-sm font-medium" @click="updateMenuState(false)">
      <IconLogin class="inline-block" />
      Login
    </router-link>
  </div>
</template>
