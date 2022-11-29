<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla Teacher</h1>
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
                ref="tea_type"
                v-model="newTeacher.tea_type"
                :rules="[() => !!name || 'This field is required']"
                :error-messages="errorMessages"
                label="Tipo"
                required
              ></v-text-field>
              <v-text-field
                ref="tea_cat"
                v-model="newTeacher.tea_cat"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Categoria"
                required
              ></v-text-field>
              <v-autocomplete
                ref="usr_id"
                :items="headers_user"
                v-model="newTeacher.usr_id"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="User"
                required
              ></v-autocomplete>
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
                @click="addTeacher"
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
                    Tabla Cursos
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
                    :items="teachers"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteCourse(item)"
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
            value: 'tea_type',
          },
          { text: 'Description', sortable: false, value: 'tea_cat' },
          { text: 'User', sortable: false, value: 'usr_id' },
          {
            text: 'Created at',
            sortable: false,
            value: 'tea_created',
          },
          {
            text: 'Updated at',
            sortable: false,
            value: 'tea_updated',
          },
          {
            text: 'Actions',
            sortable: false,
            value: 'action',
          }
        ],
        teachers: [],
        newTeacher: {},
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
        addTeacher() {
          axios.post(this.URL + '/create_teacher', this.newTeacher, this.config_request)
          .then((res) => {
            this.teachers.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newTeacher = {};
        },
        deleteTeacher(item) {
          axios.delete(this.URL + '/delete_teacher/' + item.cur_id, this.config_request)
          .then((res) => {
            this.teachers.splice(this.teachers.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        }
    },
    created() {
        axios.get(this.URL + '/teachers')
        .then((res) => { this.teachers = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>