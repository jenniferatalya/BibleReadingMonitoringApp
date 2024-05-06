import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import router from '@/router'
import App from './App.vue'
import { createVuetify } from 'vuetify'
import { createApp } from 'vue'

const app = createApp(App)
app.use(createVuetify())
app.use(router)

app.mount('#app')
