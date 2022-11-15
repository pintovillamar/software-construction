<template>
    <v-app>
  
      <v-main>
        <v-container>
          <v-switch 
            :value="darkMode" 
            @change="toggleDarkMode" 
            :label="`toggle ${switchLabel} mode`"
          ></v-switch>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    name: 'App',
    data: () => ({ 
        darkMode: false
      }),
      methods: {
        toggleDarkMode: function () {
          this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
          this.darkMode = !this.darkMode;
        }
      },
      computed: {
        switchLabel: function () {
          return this.darkMode ? 'light' : 'dark';
        }
      }
  };
  </script>
  