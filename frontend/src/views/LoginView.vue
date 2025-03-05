<script setup>
import { ref } from "vue";
import { login } from "../auth.js";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const password = ref("");
const errorMessage = ref("");


async function handleLogin() {
    try {
        await login(username.value, password.value);
        router.push("/characters"); // Redirect after login
    } catch (error) {
        errorMessage.value = "Invalid username or password.";
    }
}
</script>


<template>
    <div class="bg-gray-100 flex items-center justify-center  min-h-screen">

        <div class="flex justify-center w-full max-w-xs">
         <form @submit.prevent="handleLogin" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">

          <div class="mb-4">
            <!-- Username -->
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" v-model="username" placeholder="Username" required />
          </div>
          <div class="mb-6 py-5">
            <!-- Password -->
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" v-model="password" type="password" placeholder="Password" required />
          </div>
            <button type="submit" class="bg-red-500 text-white px-4 py-2 rounded">Login</button>
        </form>
        </div>
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

    </div>
</template>
