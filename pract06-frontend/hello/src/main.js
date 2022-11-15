// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import vue-resource from 'vue-resource'
import VueResource from 'vue-resource'
Vue.use (VueResource);

// import vue-route from 'vue-route'
import VueRouter from 'vue-router'
Vue.use (VueRouter);

import VueComponent from './components/VueComponent'
import User from './components/User'

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { // primero muestra el componente User
      path: '/',
      component: User
    },
    { // component: Data
      path: '/data',
      component: VueComponent
    }
  ]
});

Vue.config.productionTip = false

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   components: { App },
//   template: '<App/>'
// })

new Vue({
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')

