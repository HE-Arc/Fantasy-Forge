<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const items = ref([]);

const fetchItems = async (path) => {
  try {
    const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}${path}`);
    items.value = res.data;
  } catch (error) {
    console.error("Error fetching details:", error);
  }
};

onMounted(() => {
  fetchItems("/classes");
});
</script>

<template>
    <div>
        <h2>Class list</h2>
        <ul>
        <li v-for="classItem in items.results" :key="classItem.index">
            <strong>{{ classItem.name }}</strong>
            <p>{{ classItem.url }}</p>
        </li>
        </ul>
    </div>
</template>