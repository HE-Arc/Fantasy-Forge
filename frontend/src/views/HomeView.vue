<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

import IconTrashcan from "@/components/icons/IconTrashcan.vue";
import IconEdit from "@/components/icons/IconEdit.vue";

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
const deleteCharacter = async (id) => {
  try {
    await axios.delete(`/api/characters/${id}/`);
    characters.value = characters.value.filter(character => character.id !== id);
  } catch (error) {
    console.error("Error deleting character:", error);
  }
};
</script>
<template>
  <div>
    <div class="flex justify-end mb-4">
      <router-link :to="{ name: 'character-new' }" class="ff-button">Add Character</router-link>
    </div>
    <ul class="list-none p-0">
      <li v-for="character in characters" :key="character.id" class="p-2 border-b border-gray-300 flex justify-between items-center">
        <span>{{ character.name }}</span>
        <div>
            <router-link :to="{ name: 'character-edit', params: { id: character.id } }">
              <IconEdit></IconEdit>
            </router-link>
            <button @click="deleteCharacter(character.id)">
              <router-link :to="{ name: 'characters' }"><IconTrashcan></IconTrashcan></router-link>
            </button>
        </div>
      </li>
    </ul>
  </div>
</template>

