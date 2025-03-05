<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

// State variables
const name = ref('');
const message = ref('');
const isEdit = ref(false); // Flag to check if we are in edit mode
const characterId = ref(null);

// Fetch character data for editing
const route = useRoute();
const router = useRouter();

// On mounted, check if we're editing (via URL param)
onMounted(async () => {
  if (route.params.id) {
    isEdit.value = true;
    characterId.value = route.params.id;
    await fetchCharacter();
  }
});

// Fetch the character data by ID (for editing)
const fetchCharacter = async () => {
  try {
    const response = await axios.get(`/api/characters/${characterId.value}/`);
    name.value = response.data.name; // Pre-fill the form with the existing data
  } catch (error) {
    message.value = 'Error fetching character data!';
    console.error(error);
  }
};

// Handle form submission (POST for create, PUT for edit)
const submitForm = async () => {
  try {
    if (isEdit.value) {
      // PUT request for editing an existing character
      const response = await axios.put(`/api/characters/${characterId.value}/`, { name: name.value });
      message.value = `Character "${response.data.name}" updated successfully!`;
    } else {
      // POST request for creating a new character
      const response = await axios.post('/api/characters/', { name: name.value });
      message.value = `Character "${response.data.name}" created successfully!`;
    }

    router.push('/characters'); // Redirect to the list page after submission
  } catch (error) {
    message.value = 'Error submitting the form!';
    console.error(error);
  }
};
</script>

<template>
  <div>
    <h2>{{ isEdit ? 'Edit' : 'Create' }} Character</h2>
    <form @submit.prevent="submitForm">
      <input v-model="name" type="text" placeholder="Character Name" required />
      <button type="submit">{{ isEdit ? 'Update' : 'Create' }} Character</button>
    </form>

    <p v-if="message">{{ message }}</p>
  </div>
</template>

<style scoped>
input {
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 8px 12px;
  background-color: blue;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
