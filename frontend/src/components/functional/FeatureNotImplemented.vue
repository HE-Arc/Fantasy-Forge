<script setup>
  import { ref } from 'vue'

  const dialog = ref(false)
  const isMobile = ref(window.innerWidth <= 768)

  window.addEventListener('resize', () => {
    isMobile.value = window.innerWidth <= 768
  })
</script>

<template>
  <div class="text-center">
    <div class="icon-row" :style="{ flexDirection: isMobile ? 'column' : 'row', width: '100%' }">
      <v-icon class="icon" icon="mdi-hammer-wrench"></v-icon>
      <v-icon class="icon" icon="mdi-account-hard-hat"></v-icon>
      <v-btn :icon="true" @click="dialog = true" class="info-btn" variant="plain"
      :ripple="false">
      <v-icon icon="mdi-information-slab-circle-outline"></v-icon>
      </v-btn>
    </div>

    <v-dialog
      v-model="dialog"
      width="auto"
    >
      <v-card
        max-width="400"
        prepend-icon="mdi-dev-to"
        text="This feature was not implemented in the current version of the website."
        title="In Development"
      >
        <template v-slot:actions>
          <v-btn
            class="ms-auto"
            text="Ok"
            @click="dialog = false"
          ></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>
.info-btn {
  --v-btn-overlay-opacity: 0;
  --v-btn-underlay-opacity: 0;
  --v-btn-padding: 0;
  padding: 0;
  font-size: 50%;
  border-radius: 0;
  background-color: transparent;
}

.info-btn:hover{
  filter: brightness(1.2);
}

.info-btn .v-btn__overlay,
.info-btn .v-btn__underlay {
  display: none !important;
}

.icon-row {
  display: flex;
  width: 100%;
}

.icon {
  max-width: 33%;
  font-size: 100%;
}
</style>
