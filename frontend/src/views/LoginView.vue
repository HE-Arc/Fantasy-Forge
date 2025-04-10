<script setup>
import { ref } from "vue";
import { login } from "../auth.js";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const password = ref("");
const errorMessage = ref("");
const isAuthenticated = ref(!!localStorage.getItem("access"));


async function handleLogin() {
    try {
      await login(username.value, password.value)
      .then(() => {
        setTimeout(() => {
          window.location.reload();
        }, 10);
      });
      isAuthenticated.value = true;
      router.push("/characters");
    } catch (error) {
        errorMessage.value = "Invalid username or password.";
    }
}
</script>


<template>
    <div class="flex items-center justify-center  min-h-screen" style="background-color: var(--color-background-soft);">

        <div class="flex justify-center w-full max-w-xs">
         <form @submit.prevent="handleLogin" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">

          <div class="mb-4">
            <!-- Username -->
            <input class="ff-input" v-model="username" placeholder="Username" required />
          </div>
          <div class="py-5">
            <!-- Password -->
            <input class="ff-input" v-model="password" type="password" placeholder="Password" required />
          </div>
            <button type="submit" class="ff-button">Login</button>
            <a class="px-4 py-2.5 rounded dark:text-gray-900" href="register">No account? Register</a>
        </form>

        </div>
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

    </div>
</template>
