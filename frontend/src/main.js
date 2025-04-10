import './assets/main.css'
import './assets/charsheet.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from "axios";

import { createVuetify } from 'vuetify'
import 'vuetify/styles'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import '@mdi/font/css/materialdesignicons.css'

const vuetify = createVuetify({
  components,
  directives,
})

axios.defaults.baseURL = import.meta.env.VITE_API_URL

const app = createApp(App)

app.use(router)
app.use(vuetify)

app.mount('#app')
