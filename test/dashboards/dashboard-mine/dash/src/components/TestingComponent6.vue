<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla Enroll</h1>
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
                ref="enr_date"
                v-model="newEnroll.enr_date"
                :rules="[() => !!name || 'This field is required']"
                :error-messages="errorMessages"
                label="Date"
                required
              ></v-text-field>
              <v-text-field
                ref="std_id"
                v-model="newEnroll.std_id"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Student"
                required
              ></v-text-field>
              <v-text-field
                ref="gru_id"
                v-model="newEnroll.gru_id"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Grupo"
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
                @click="addEnroll"
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
                    Tabla Enroll
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
                    :items="enrolls"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteEnroll(item)"
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
            value: 'enr_date',
          },
          { text: 'Description', sortable: false, value: 'std_id' },
          { text: 'User', sortable: false, value: 'gru_id' },
          {
            text: 'Created at',
            sortable: false,
            value: 'enr_created',
          },
          {
            text: 'Updated at',
            sortable: false,
            value: 'enr_updated',
          },
          {
            text: 'Actions',
            sortable: false,
            value: 'action',
          }
        ],
        enrolls: [],
        newEnroll: {},
        user:[],
        headers_user: [{value:"usr_id"}],
        URL: 'http://localhost:5000',
        config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
      }
    },
    methods: {
        addEnroll() {
          axios.post(this.URL + '/create_enroll', this.newEnroll, this.config_request)
          .then((res) => {
            this.enrolls.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newEnroll = {};
        },
        deleteEnroll(item) {
          axios.delete(this.URL + '/delete_enroll/' + item.enr_id, this.config_request)
          .then((res) => {
            this.enrolls.splice(this.enrolls.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        }
    },
    created() {
        axios.get(this.URL + '/enrolls')
        .then((res) => { this.enrolls = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>