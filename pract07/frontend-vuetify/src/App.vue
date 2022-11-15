<template>
  <v-app>
    <v-main>
      <UserData/>
      <DarkMode/>
    </v-main>
  </v-app>
</template>

<script>
import DarkMode from './components/DarkMode.vue';
import UserData from './components/UserData.vue';


export default {
  name: 'App',

  components: {
    DarkMode,
    UserData,
  },

  data: () => ({
    //
  }),
};
</script>
