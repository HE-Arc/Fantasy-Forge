<script setup>
import axios from "axios";
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const items = ref([]);

const getPath = () => {
  return Array.isArray(route.params.name) ? route.params.name.join("/") : route.params.name;
}

const fetchItems = async (path) => {
  try {
    const res = await axios.get(`${import.meta.env.VITE_DND_API_URL}${path}`);
    
    items.value = res.data;
  } catch (error) {
    console.error("Error fetching items:", error);
    router.push({ name: "rules" });
  }
};

onMounted(() => {
  fetchItems(getPath());
});

// to watch for changes in the route and update the items
watch(
  () => route.params.name, 
  () => fetchItems(getPath()), 
  { immediate: true }
);

</script>

<template>
    <div>
      {{ items }}
      <!--
        <h2>{{ route.params.name }} list</h2>
        <ul>
        <li v-for="item in items.results" :key="item.index">
            <strong>{{ item.name }}</strong>
            <p><router-link :to="{ name: 'rules', params: { name: [route.params.name, item.index] } }">{{ item.url }}</router-link></p>
        </li>
        </ul>
      -->
    </div>
</template>