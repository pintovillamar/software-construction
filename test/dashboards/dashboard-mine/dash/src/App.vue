<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Asistencia - vuetify
          </v-list-item-title>
          <v-list-item-subtitle>
            Universidad La Salle
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :color="item.color"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content class="test">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        
      <v-toolbar-title>Test</v-toolbar-title>
      
    </v-app-bar>
    

    <v-main>
      <!--  -->
      <router-view></router-view>
    </v-main>

      <!-- <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >

      <v-card-text class="footer">
        Asistencia © Universidad La Salle {{ new Date().getFullYear() }} | Hecho con <a href="https://vuetifyjs.com/">Vuetify</a>.
      </v-card-text>
    </v-card>
  </v-footer> -->

  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: null,
      items: [
          { title: 'Inicio', icon: 'mdi-home-account',to: '/', color: 'blue'},
          { title: 'Asistencia', icon: 'mdi-checkbox-marked-circle',to: '/asistencia', color:'green'},
          
          // { title: 'Testing Enviroment', icon: 'mdi-test-tube',to: "/test", color:'orange'},
          { title: 'Face Detection', icon: 'mdi-face-recognition',to: "/face", color:'red'},
          { title: 'Roles', icon: 'mdi-shield-crown-outline',to: "/roles", color:'blue'},
          { title: 'User', icon: 'mdi-account',to: "/user", color:'blue'},
          { title: 'Group', icon: 'mdi-account-group',to: "/group", color:'blue'},
          { title: 'Course', icon: 'mdi-book',to: "/course", color:'blue'},
          { title: 'Teacher', icon: 'mdi-human-male-board',to: "/teacher", color:'blue'},
          { title: 'Enroll', icon: 'mdi-book-arrow-up-outline',to: "/enroll", color:'blue'},
          { title: 'Schedule', icon: 'mdi-calendar-month',to: "/schedule", color:'blue'},
          { title: 'Acerca de', icon: 'mdi-help',to: "/about", color:'purple'}
        ]
    }),
  }
</script>

<style>
.footer{
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 50px;
  background-color:black;
  text-align: center;
}
</style>