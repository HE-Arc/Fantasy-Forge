<script setup>
import axios from "axios";
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const items = ref([]);
const abilityDetails = ref({});

const categories = ref(["ability-scores", "classes", "skills"]);

const getPath = () => {
  return Array.isArray(route.params.name) ? route.params.name.join("/") : route.params.name;
};

// Fetch general items
const fetchItems = async (path) => {
  try {
    const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}${path}`);
    items.value = res.data;

    // If we are on "ability-scores", fetch individual details
    if (route.params.name === "ability-scores" && res.data.results) {
      await fetchAbilityDetails(res.data.results);
    }
  } catch (error) {
    console.error("Error fetching items:", error);
    router.push({ name: "rules" }).then(() => window.location.reload());
  }
};

// Fetch details for each ability
const fetchAbilityDetails = async (abilities) => {
  const details = {};
  await Promise.all(
    abilities.map(async (ability) => {
      try {
        const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}ability-scores/${ability.index}`);
        details[ability.index] = res.data;
      } catch (error) {
        console.error(`Error fetching ${ability.index}:`, error);
      }
    })
  );
  abilityDetails.value = details; // Assign once to trigger reactivity
};

// Fetch when component mounts
onMounted(() => {
  fetchItems(getPath());
  fetchAbilityDetails();
});

// Watch route changes and refetch data
watch(
  () => route.params.name,
  () => fetchItems(getPath()),
  { immediate: true }
);
</script>

<template>
  <div>
    <h1>
      {{
        (Array.isArray(route.params.name) ? route.params.name.at(-1) : route.params.name || "RULES")
          .replace("-", " ")
          .toUpperCase()
      }}
    </h1>

    <div v-if="!route.params.name">
      <p>Choose a category from the list below:</p>
      <ul>
        <li v-for="category in categories" :key="category">
          <router-link :to="{ name: 'rules', params: { name: category } }">
            {{ category.replace("-", " ").toUpperCase() }}
          </router-link>
        </li>
      </ul>
    </div>

    <div v-else>
      <div class="cards-container">
        <div v-for="item in items.results" :key="item.index" class="card">
          <div v-if="route.params.name === 'ability-scores'">
            <h2>{{ abilityDetails[item.index]?.name }}</h2>
            <h3>{{ abilityDetails[item.index]?.full_name }}</h3>
            <p v-for="desc in abilityDetails[item.index]?.desc" :key="desc">{{ desc }}</p>
          </div>
          <div v-else>
            <h2>{{ item.name }}</h2>
          </div>
        </div>
      </div>
      <a @click="router.back()">Back</a>
    </div>
  </div>
</template>

<style scoped>
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  padding: 1rem;
}

.card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  font-weight: bold;
}

h2 {
  font-size: 1.5rem;
  font-weight: bold;
}

h3 {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 0.5rem;
}

p {
  color: #333;
  margin-bottom: 0.5rem;
}
</style>
