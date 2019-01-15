import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import '@/assets/css/style.css'

Vue.use(Buefy)
Vue.config.productionTip = false

Vue.filter('capitalize', (value) => {
  if (!value) return ''
  value = value.toString().toLowerCase()
  if (value.length > 43) {
    value.substring(39)
    const space = value.lastIndexOf(' ')
    value.substring(space)
    value = `${value} ...`
  }
  return value.charAt(0).toUpperCase() + value.slice(1)
})

const token = localStorage.getItem('user-token')

axios.defaults.baseURL = process.env.VUE_APP_ROOT_API

if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
