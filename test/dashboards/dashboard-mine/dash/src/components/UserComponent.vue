<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla User</h1>
            </v-col>
        </v-row>

          <v-row justify="center">
        <v-col
          cols="12"
          sm="10"
          md="8"
          lg="6"
        >
          <v-card ref="form">
            <v-card-text>
              <v-text-field
                ref="usr_name"
                v-model="newUser.usr_name"
                label="Nombres"
                required
              ></v-text-field>
              <v-text-field
                ref="usr_last_name"
                v-model="newUser.usr_last_name"
                label="Apellidos"
                required
              ></v-text-field>
            <v-text-field
                ref="usr_dni"
                v-model="newUser.usr_dni"
                label="DNI"
                required
            ></v-text-field>

            
            <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                :return-value.sync="date"
                transition="scale-transition"
                offset-y
                min-width="auto"
            >
                <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="date"
                    label="Fecha de Nacimiento"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
                </template>
                <v-date-picker
                v-model="date"
                no-title
                scrollable
                >
                <v-spacer></v-spacer>
                <v-btn
                    text
                    color="primary"
                    @click="menu = false"
                >
                    Cancel
                </v-btn>
                <v-btn
                    text
                    color="primary"
                    @click="$refs.menu.save(date)"
                >
                    OK
                </v-btn>
                </v-date-picker>
            </v-menu>

            
            <v-text-field
                ref="usr_email"
                v-model="newUser.usr_email"
                label="Correo electrónico"
                required
            ></v-text-field>
            <v-text-field
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                ref="usr_password"
                :type="show1 ? 'text' : 'password'"
                v-model="newUser.usr_password"
                label="Contraseña"
                @click:append="show1 = !show1"
                
                required
            ></v-text-field>
            <!-- <v-text-field
                ref="usr_photo"
                v-model="newUser.usr_photo"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Foto"
                required
            ></v-text-field> -->

            <template>
              <v-file-input
                show-size
                counter
                multiple
                label="Foto"
              ></v-file-input>
            </template>

            <v-text-field
                ref="ust_id"
                v-model="newUser.ust_id"
                label="Rol"
                required
            ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn text>
                Cancel
              </v-btn>
              <v-spacer></v-spacer>
              <v-slide-x-reverse-transition>
                <v-tooltip
                  left
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      icon
                      class="my-0"
                      v-bind="attrs"
                      @click="resetForm"
                      v-on="on"
                    >
                      <v-icon>mdi-refresh</v-icon>
                    </v-btn>
                  </template>
                  <span>Refresh form</span>
                </v-tooltip>
              </v-slide-x-reverse-transition>
              <v-btn
                color="primary"
                text
                @click="addUser"
              >
                Submit
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
    </v-row>

        <v-row>
            <v-col>
                <v-card>
                    <v-card-title>
                    Roles
                    <v-spacer></v-spacer>
                    <v-text-field
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="Search"
                        single-line
                        hide-details
                    ></v-text-field>
                    </v-card-title>
                    <v-data-table
                    :headers="headers"
                    :items="users"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteUser(item)"
                      >
                      <v-icon>mdi-delete</v-icon>
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-card>
            </v-col>
        </v-row>

    </v-container>
</template>

<script>
import axios from 'axios';

  export default {
    name: 'Testing2',

    data () {
      return {
        
        date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        menu: false,
        modal: false,
        menu2: false,
        show1: false,


        search: '',
        headers: [
            { text: 'Nombres', value: 'usr_name' },
            { text: 'Apellidos', value: 'usr_last_name' },
            { text: 'DNI', value: 'usr_dni' },
            { text: 'Fecha de nacimiento', value: 'usr_dob' },
            { text: 'Correo electrónico', value: 'usr_email' },
            // { text: 'Contraseña', value: 'usr_password' },
            { text: 'Foto', value: 'usr_photo' },
            { text: 'Rol', value: 'ust_id' },
            { text: 'Created at', sortable: false, value: 'usr_created' },
            { text: 'Updated at', sortable: false, value: 'usr_updated' },
            { text: 'Actions', sortable: false, value: 'action' }
        ],
        users: [],
        newUser: {},
        URL: 'http://localhost:5000',
        config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
      }
    },

    methods: {

        formatDate (date) {
            if (!date) return null

            const [year, month, day] = date.split('-')
            return `${day}/${month}/${year}`
        },

        parseDate (date) {
            if (!date) return null

            const [month, day, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },

        addUser() {
          axios.post(this.URL + '/create_user', this.newUser, this.config_request)
          .then((res) => {
            this.users.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newUser = {};
        },
        deleteUser(item) {
          axios.delete(this.URL + '/delete_user/' + item.usr_id, this.config_request)
          .then((res) => {
            this.user.splice(this.user.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        },
        save (date) {
            this.$refs.menu.save(date)
        },
        resetForm() {
          this.newUser = {};
        },
    },
    created() {
        axios.get(this.URL + '/users', this.config_request)
        .then((res) => { this.users = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>