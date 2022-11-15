<template>
  <div id="app">
    <GroupData/>
    <UserData/>
  </div>
</template>

<script>
import GroupData from './components/GroupData.vue'
import UserData from './components/UserData.vue'

export default {
  name: 'App',
  components: {
    GroupData,
    UserData
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} 
</style>
