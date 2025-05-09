<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

import IconTrashcan from "@/components/icons/IconTrashcan.vue";
import IconEdit from "@/components/icons/IconEdit.vue";

const characters = ref([]);
const isAuthenticated = ref(!!localStorage.getItem("access"));

const fetchCharacters = async () => {
  try {

    const token = localStorage.getItem("access");

    if (!token) {
      console.error("Missing token, please log in again.");
      return;
    }

    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    };

    const res = await axios.get("/api/characters/", config).then(response => {
    characters.value = response.data;
  });

    //characters.value = res.data;

  } catch (error) {
    console.error("Error fetching characters:", error);
  }
};

onMounted(() => {
  fetchCharacters();
});

const deleteCharacter = async (id) => {
  const confirmDelete = confirm("Are you sure you want to delete this character?");
  if (!confirmDelete) return;

  try {
    const token = localStorage.getItem("access");

    if (!token) {
      console.error("Missing token, please log in again.");
      return;
    }

    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    };

    await axios.delete(`/api/characters/${id}/`, config);
    characters.value = characters.value.filter(character => character.id !== id);
  } catch (error) {
    console.error("Error deleting character:", error);
  }
};


</script>
<template>
  <div>
    <div class="container mx-auto px-2 py-4">
      <h1 class="text-4xl font-bold mb-8">Character List - How does it work?</h1>
    </div>
    <div class="container mx-auto px-2 py-4">
      <p>On this page, you see the list of (currently all existent, but later-) the characters you or your friends created. You can create new ones, delete existent, or click them to see and edit their full character sheet (currently not present).</p>
   </div>

    <div class="flex justify-end mb-4">
      <router-link :to="{ name: 'character-new' }" class="ff-button">Add Character</router-link>
    </div>
    <ul class="list-none p-0">
      <li v-for="character in characters" :key="character.id" class="p-2 border-b border-gray-300 flex justify-between items-center">
        <span>
          <div>
            <strong>{{ character.name }}</strong> | Class: {{ character.job }}
          </div>
          <div>
            Strength: {{ character.strength }} | Dexterity: {{ character.dexterity }} | Constitution: {{ character.constitution }} | Intelligence: {{ character.intelligence }} | Wisdom: {{ character.wisdom }} | Charisma: {{ character.charisma }}
          </div>
        </span>
        <div>
            <router-link :to="{ name: 'character-edit', params: { id: character.id } }">
              <IconEdit></IconEdit>
            </router-link>
            <button @click="deleteCharacter(character.id)">
              <IconTrashcan></IconTrashcan>
            </button>
        </div>
      </li>
    </ul>
  </div>
</template>

