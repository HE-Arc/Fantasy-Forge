<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from 'vue-router';
import NumberInput from '@/components/functional/NumberInput.vue';
import { resolveComponent } from "vue";

// State variables
const char_name = ref('');
const strength_stat = ref(0);
const dexterity_stat = ref(0);
const constitution_stat = ref(0);
const intelligence_stat = ref(0);
const wisdom_stat = ref(0);
const charisma_stat = ref(0);
const characterId = ref(null);
const char_biography = ref('');
const showAlert = ref(false);
const newOwnerName = ref('');
const activeIndex = ref(-1);
const filteredUsers = ref([]);

// Fetch character data for editing
const route = useRoute();

onMounted(async () => {
  if (route.params.id) {
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
    strength_stat.value = response.data.strength;
    dexterity_stat.value = response.data.dexterity;
    constitution_stat.value = response.data.constitution;
    intelligence_stat.value = response.data.intelligence;
    wisdom_stat.value = response.data.wisdom;
    charisma_stat.value = response.data.charisma;
    char_biography.value = response.data.biography;
  } catch (error) {
    console.error(error);
  }
};

const addOwner = async () => {
  if (!newOwnerName.value || !characterId.value) return;

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

    const payload = {
      owner_name: newOwnerName.value,
    };

    await axios.post(`/api/characters/${characterId.value}/add_ownership/`, payload, config);

    showAlert.value = true;

    setTimeout(() => {
      showAlert.value = false;
    }, 5000);

    newOwnerName.value = ''; 

  } catch (error) {
    console.error(error);
  }
};

const saveChanges = async () => {
  if (!characterId.value) return;

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

    const payload = {
      strength: strength_stat.value,
      dexterity: dexterity_stat.value,
      constitution: constitution_stat.value,
      intelligence: intelligence_stat.value,
      wisdom: wisdom_stat.value,
      charisma: charisma_stat.value,
      biography: char_biography.value,
    };

    await axios.patch(`/api/characters/${characterId.value}/`, payload, config);

    // show alert about successfull edit
    showAlert.value = true;

    // auto-hide alert after 5 seconds
    setTimeout(() => {
      showAlert.value = false;
    }, 5000);

  } catch (error) {
    console.error(error);
  }
};

// handle user search

const searchUsers = async () => {
  if (!newOwnerName.value) {
    filteredUsers.value = [];
    return;
  }

  try {
    const token = localStorage.getItem("access");

    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    const response = await axios.get(`/api/auth/search_users/?username=${newOwnerName.value}`, config);

    filteredUsers.value = response.data;
    activeIndex.value = -1;

  } catch (error) {
    console.error("Error searching users:", error);
  }
};

const selectUser = (user) => {
  newOwnerName.value = user.username;
  filteredUsers.value = [];
};

const moveDown = () => {
  if (filteredUsers.value.length === 0) return;
  activeIndex.value = (activeIndex.value + 1) % filteredUsers.value.length;
};

const moveUp = () => {
  if (filteredUsers.value.length === 0) return;
  activeIndex.value = (activeIndex.value - 1 + filteredUsers.value.length) % filteredUsers.value.length;
};

const selectActive = () => {
  if (activeIndex.value >= 0 && activeIndex.value < filteredUsers.value.length) {
    selectUser(filteredUsers.value[activeIndex.value]);
  }
};

const clearSuggestions = () => {
  setTimeout(() => {
    filteredUsers.value = [];
    activeIndex.value = -1;
  }, 150);
};


</script>

<template>
<v-alert
  v-if="showAlert"
  color="success"
  icon="$success"
  title="Saved changes"
  text="Your changes were successfully saved"
  closable
></v-alert>

<div class="container mx-auto px-2 py-4">

  <div class="flex justify-between mb-4">
    <div style="align-content: left;">
    <button type="submit" @click="saveChanges" class="ff-button">Save changes</button>
  </div>
  <form @submit.prevent="addOwner" class="relative flex items-start gap-2 w-full max-w-xl">
    <div class="relative flex-1">
      <input
        type="text"
        v-model="newOwnerName"
        @input="searchUsers"
        @keydown.down.prevent="moveDown"
        @keydown.up.prevent="moveUp"
        @keydown.enter.prevent="selectActive"
        @blur="clearSuggestions"
        placeholder="Owner username"
        required
        class="w-full px-3 py-2 border rounded"
      />

      <ul
        v-if="filteredUsers.length"
        class="absolute z-50 w-full border border-gray-300 rounded shadow-md bg-white max-h-60 overflow-auto"
      >
        <li
          v-for="(user, index) in filteredUsers"
          :key="user.id"
          @click="selectUser(user)"
          :class="[
            'px-3 py-2 cursor-pointer hover:bg-gray-100',
            index === activeIndex ? 'bg-blue-500 text-white' : ''
          ]"
        >
          {{ user.username }}
        </li>
      </ul>
    </div>

    <button type="submit" class="ff-button">Add owner</button>
  </form>
</div>


    <div class="charsheet">
    <div class="sheet-grid-section">
  <div class="sheet-namelvl sheet-block">
    <label>Name</label>
    <div style="font-weight: 700;">{{char_name}}</div>
  </div>
  <div class="sheet-class sheet-block">
    <span>Class</span>
  </div>
  <div class="sheet-stat sheet-block">
    <div><NumberInput
      v-model:value = "strength_stat"
      name = "Strength"
    ></NumberInput></div>
    <span><NumberInput
      v-model:value="dexterity_stat"
      name = "Dexterity"
    ></NumberInput></span>
    <span><NumberInput
      v-model:value="constitution_stat"
      name = "Constitution"
    ></NumberInput></span>
    <span><NumberInput
      v-model:value="intelligence_stat"
      name = "Intelligence"
    ></NumberInput></span>
    <span><NumberInput
      v-model:value="wisdom_stat"
      name = "Wisdom"
    ></NumberInput></span>
    <span><NumberInput
      v-model:value="charisma_stat"
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
    <v-textarea
      class="w-100"
      label="Biography"
      prepend-icon="mdi-script-text-outline"
      v-model:model-value="char_biography"
      name="input-7-1"
      variant="filled"
      rows="auto"
      auto-grow
    ></v-textarea>
  </div>
  <div class="sheet-notes sheet-block">
    <h3>Notes (logs)</h3>
    <span>TODO : list</span>
    <div style="align-content: right;">

    <a class="px-4 py-2.5 text-red-700 hover:text-red-100 rounded dark:text-gray-900 " href="">View all logs</a>
  </div>
  </div>
</div>
</div>


</div>


</template>


