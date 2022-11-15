<template>
  <div id="app">
    <User_type/>
    <User/>
    <Group/>
  </div>
</template>

<script>
import User from './components/Users.vue'
import User_type from './components/User_type.vue';
import Group from './components/Group.vue';

export default {
  name: 'App',
  components: {
    User,
    User_type,
    Group
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
  margin-top: 60px;
}
</style>
