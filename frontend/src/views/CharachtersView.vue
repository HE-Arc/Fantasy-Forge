<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
const characters = ref([]);

const fetchCharacters = async () => {
  try {
    const res = await axios.get("/api/characters/");
    characters.value = res.data;
  } catch (error) {
    console.error("Error fetching characters:", error);
  }
};

onMounted(() => {
  fetchCharacters();
});
</script>
<template>
  <div>
    <ul>
      <li v-for="character in characters" :key="character.id">
        {{ character.name }}
      </li>
    </ul>
  </div>
</template>
