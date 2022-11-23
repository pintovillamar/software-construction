<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla User Type</h1>
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
                ref="ust_name"
                v-model="newUserType.ust_name"
                :rules="[() => !!name || 'This field is required']"
                :error-messages="errorMessages"
                label="Rol"
                required
              ></v-text-field>
              <v-text-field
                ref="ust_desc"
                v-model="newUserType.ust_desc"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Descripción"
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
                  v-if="formHasErrors"
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
                @click="addUserType"
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
                    :items="user_types"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteUserType(item)"
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
    name: 'Testing',

    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Rol',
            align: 'start',
            sortable: false,
            value: 'ust_name',
          },
          { text: 'Description', sortable: false, value: 'ust_desc' },
          {
            text: 'Created at',
            sortable: false,
            value: 'ust_created',
          },
          {
            text: 'Updated at',
            sortable: false,
            value: 'ust_updated',
          },
          {
            text: 'Actions',
            sortable: false,
            value: 'action',
          }
        ],
        user_types: [],
        newUserType: {},
        URL: 'http://localhost:5000',
        config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
      }
    },
    methods: {
        addUserType() {
          axios.post(this.URL + '/create_user_type', this.newUserType, this.config_request)
          .then((res) => {
            this.user_types.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newUserType = {};
        },
        deleteUserType(item) {
          axios.delete(this.URL + '/delete_user_type/' + item.ust_id, this.config_request)
          .then((res) => {
            this.user_types.splice(this.user_types.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        }
    },
    created() {
        axios.get(this.URL + '/user_types')
        .then((res) => { this.user_types = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>