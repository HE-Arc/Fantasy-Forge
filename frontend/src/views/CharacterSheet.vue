<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from 'vue-router';
import NumberInput from '@/components/functional/NumberInput.vue';

// State variables
const char_name = ref('');
const message = ref('');
const isEdit = ref(false); // Flag to check if we are in edit mode
const characterId = ref(null);

// Fetch character data for editing
const route = useRoute();
const router = useRouter();

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

    const token = localStorage.getItem("access");

    console.log(token);

    if (!token) {
      console.error("Missing token, please log in again.");
      return;
    }

    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    };

    const response = await axios.get(`/api/characters/${characterId.value}/`, config);
    char_name.value = response.data.name; // Pre-fill the form with the existing data
  } catch (error) {
    message.value = 'Error fetching character data!';
    console.error(error);
  }
};
</script>

<template>

<div class="container mx-auto px-2 py-4">


<div style="text-align: right;">
  <form @submit.prevent="addOwner">
    <!-- TODO search among users via SearchElement? -->
      <input type="text" placeholder="Owner id" required />
      <button type="submit" class="ff-button">Add owner</button>
    </form>
  </div>

    <!-- TODO make the button to the right corner -->
    <div style="align-content: right;">
    <button type="submit" class="ff-button">Save changes</button>
    </div>

    <div class="charsheet">
    <div class="sheet-grid-section">
  <div class="sheet-namelvl sheet-block">
    <label>Name</label>
    <h1>(Character name) : {{char_name}}</h1>
  </div>
  <div class="sheet-class sheet-block">
    <span>Class</span>
  </div>
  <div class="sheet-stat sheet-block">
    <div><NumberInput
      name = "Strength"
    ></NumberInput></div>
    <span><NumberInput
      name = "Dexterity"
    ></NumberInput></span>
    <span><NumberInput
      name = "Constitution"
    ></NumberInput></span>
    <span><NumberInput
      name = "Intelligence"
    ></NumberInput></span>
    <span><NumberInput
      name = "Wisdom"
    ></NumberInput></span>
    <span><NumberInput
      name = "Charisma"
    ></NumberInput></span>
  </div>
  <div class="sheet-skills sheet-block">
    <h3>Skills</h3>
    <label><button name="roll_str" value="/r 1d6+@{str}" type="roll"></button> acrobatics <input type="number" name="attr_str"></label>
    <label><button name="roll_agi" value="/r 1d6+@{agi}" type="roll"></button> history <input type="number" name="attr_agi"></label>
    <label><button name="roll_mind" value="/r 1d6+@{mind}" type="roll"></button> animal handling <input type="number" name="attr_mind"></label>
  </div>
  <div class="sheet-bio sheet-block">
    <h3>Biography</h3>
  </div>
  <div class="sheet-notes sheet-block">
    <h3>Notes (logs)</h3>
    <span>TODO : list</span>
  </div>
</div>
</div>


</div>


</template>


