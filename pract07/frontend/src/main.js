import Vue from 'vue'
import App from './App'

// import vue-resource from 'vue-resource'
import VueResource from 'vue-resource'
Vue.use ( VueResource );

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App)
})
