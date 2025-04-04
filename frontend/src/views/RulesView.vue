<script setup>
import axios from "axios";
import { ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const items = ref([]);
const abilityDetails = ref({});
const classDetails = ref({});
const skillDetails = ref({});

const categories = ref(["ability-scores", "classes", "skills"]);

const getPath = () => {
  return Array.isArray(route.params.name) ? route.params.name.join("/") : route.params.name;
};

// Fetch general items
const fetchItems = async (path) => {
  try {
    const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}${path}`);
    items.value = res.data;

    if (path === "ability-scores") {
      abilityDetails.value = await fetchDetails(items.value.results, path);
    }
    if (path === "classes") {
      classDetails.value = await fetchDetails(items.value.results, path);
    }
    if (path === "skills") {
      skillDetails.value = await fetchDetails(items.value.results, path);
    }

  } catch (error) {
    console.error("Error fetching items:", error);
    router.push({ name: "rules" }).then(() => window.location.reload());
  }
};

// Fetch details for each item in the category
const fetchDetails = async (categoryItems, path) => {
  const details = {};
  await Promise.all(
    categoryItems.map(async (item) => {
      try {
        const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}${path}/${item.index}`);
        details[item.index] = res.data;
      } catch (error) {
        console.error(`Error fetching ${item.index}:`, error);
      }
    })
  );
  return details;
};

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
      <p v-if="items?.results?.length && classDetails[items.results[0]?.index]">
        More details about proficiency choices can be found in <router-link :to="{ name: 'rules', params: { name: 'skills' } }">skills</router-link>.
      </p>
      <div class="cards-container">
        <div v-for="item in items.results" :key="item.index" class="card">
          <div v-if="abilityDetails[item.index]">
            <h2>{{ abilityDetails[item.index]?.name }}</h2>
            <h3>{{ abilityDetails[item.index]?.full_name }}</h3>
            <p v-for="desc in abilityDetails[item.index]?.desc" :key="desc">{{ desc }}</p>
          </div>

          <div v-else-if="classDetails[item.index]">
            <h2>{{ classDetails[item.index]?.name }}</h2>
            <h3>HP {{ classDetails[item.index]?.hit_die }}</h3>
            <section>
              <h3>Proficiency choices</h3>
              <p v-for="choice in classDetails[item.index]?.proficiency_choices" :key="choice.index">
                {{ choice.desc }}
              </p>
            </section>
            <section>
              <h3>Proficiencies</h3>
              <ul>
                <li v-for="proficiency in classDetails[item.index]?.proficiencies" :key="proficiency.index">
                  {{ proficiency.name }}
                </li>
              </ul>
            </section>
            <section>
              <h3>Starting equipment options</h3>
              <ul>
                <li v-for="option in classDetails[item.index]?.starting_equipment_options" :key="option.index">
                  {{ option.desc }}
                </li>
              </ul>
            </section>
          </div>

          <div v-else-if="skillDetails[item.index]">
            <h2>{{ skillDetails[item.index]?.name }}</h2>
            <p v-for="desc in skillDetails[item.index]?.desc" :key="desc">{{ desc }}</p>
          </div>

          <div v-else>
            <h2>{{ item.name }}</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  font-weight: bold;
}
</style>
