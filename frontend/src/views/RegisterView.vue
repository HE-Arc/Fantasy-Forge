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
        errorMessage.value = "Registration failed. Try again."; //+ error.response.data;
    }
}
</script>

<template>
    <div>
      <div class="bg-gray-100 flex items-center justify-center  min-h-screen">

        <div class="flex justify-center w-full max-w-xs">

        <form @submit.prevent="handleRegister" class="bg-white shadow-md rounded px-8 pt-6 pb-8">
          <div class="mb-6">
          <input class="mb-10 shadow appearance-none border rounded w-full py-20 px-3 text-gray-700 focus:outline-none focus:shadow-outline " v-model="username" placeholder="Username" required />
            </div>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" v-model="email" placeholder="Email" required />
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" v-model="password" type="password" placeholder="Password" required />
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" v-model="password2" type="password" placeholder="Confirm Password" required />
            <button class="bg-red-500 text-white px-4 py-2 rounded" type="submit">Register</button>
        </form>
      </div>
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
        </div>
    </div>
</template>
