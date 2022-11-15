<template>
  <div id="app">
    <!-- <VueMethods/>
    <VueComponent msg="1"/>
    <SimpleComponent/> -->
    <!-- <User/> -->
    <nav>
      <li>
        <router-link to="/data">Data</router-link>
      </li>
      <li>
        <router-link to="/">User</router-link>
      </li>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import SimpleComponent from './components/SimpleComponent.vue'
import VueComponent from './components/VueComponent.vue'
import VueMethods from './components/VueMethods.vue'
import User from './components/User.vue'

export default {
  name: 'App',
  components: {
    SimpleComponent,
    VueComponent,
    VueMethods,
    User
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
