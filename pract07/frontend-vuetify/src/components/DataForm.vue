<template>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="name"
              
              label="Name"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="calories"

              label="Calories"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="fats"
              
              label="Fats"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="carbohydrates"
              
              label="Carbohydrates"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="proteins"
              
              label="Proteins"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="1"
          >
            <v-text-field
              v-model="iron"
              
              label="Iron %"
              required
            ></v-text-field>
          </v-col>

          <v-btn @click="addDessert"
          class="mr-3" type="submit" :disabled="invalid"
            >
                submit
            </v-btn>
            <v-btn @click="clear">
                clear
        </v-btn>
  
          
        </v-row>
      </v-container>
    </v-form>
  </template>

<script>
  export default {
    data: () => ({
      valid: false,
      firstname: '',
      lastname: '',
    }),
    methods: {
      clear () {
        this.valid = false
        this.name = ''
        this.calories = ''
        this.fats = ''
        this.carbohydrates = ''
        this.proteins = ''
        this.iron = ''
      },
      submit () {
        console.log('Submitted')
      },
        addDessert: function (  ) {
            this.desserts.push({
                name: this.name,
                calories: this.calories,
                fats: this.fats,
                carbohydrates: this.carbohydrates,
                proteins: this.proteins,
                iron: this.iron
            })
        }
    },
    
  }
</script>