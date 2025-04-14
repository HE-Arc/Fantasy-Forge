<script setup>
import { ref } from "vue";
import { register } from "../auth.js";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const email = ref("");
const password = ref("");
const password2 = ref("");
const errorMessage = ref("");

async function handleRegister() {
  try {
    await register(username.value, email.value, password.value, password2.value);
    router.push("/login"); // Redirect to login after registration
  } catch (error) {
    if (error && typeof error === "object") {
      errorMessage.value = Object.values(error).flat().join(" ");
    } else {
      errorMessage.value = "Registration failed. Try again.";
    }
  }
}

</script>

<template>
  <div>
    <div class="flex items-center justify-center min-h-screen" style="background-color: var(--color-background-soft);">
      <div class="flex flex-col items-center w-full max-w-xs">

        <!-- Error Message Box -->
        <transition name="fade">
          <div v-if="errorMessage"
            class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4 w-full max-w-xs text-sm shadow">
            <strong class="font-bold">Login failed:</strong>
            <span class="block sm:inline ml-1">{{ errorMessage }}</span>
          </div>
        </transition>


        <!-- Registration Form -->
        <form @submit.prevent="handleRegister" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full">
          <div class="py-2">
            <input class="ff-input" v-model="username" placeholder="Username" required />
          </div>
          <div class="py-2">
            <input class="ff-input" v-model="email" placeholder="Email" required />
          </div>
          <div class="py-2">
            <input class="ff-input" v-model="password" type="password" placeholder="Password" required />
          </div>
          <div class="py-2">
            <input class="ff-input" v-model="password2" type="password" placeholder="Confirm Password" required />
          </div>
          <div class="py-3">
            <button class="ff-button" type="submit" autofocus>Register</button>
          </div>
        </form>

      </div>
    </div>
  </div>
</template>
