<template>
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <v-img
            :src="require('../assets/lasalle-logo.svg')"
            class="my-3"
            contain
            height="30vh"
          />
        </v-col>
  
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            Bienvenido al nuevo portal de Asistencia
          </h1>
        </v-col>
      </v-row>
    </v-container>

  </template>
  
  <script>
    export default {
      name: 'InicioComponente',
  
      data: () => ({
        
      }),
    }
  </script>
  