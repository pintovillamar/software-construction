<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla Group</h1>
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
                ref="gru_name"
                v-model="newGroup.gru_name"
                label="Name"
                required
              ></v-text-field>
              <v-combobox
                v-model="newGroup.tea_id"
                :items="teachers"
                item-text="title"
                item-value="id"
                label="Teacher"          
                outlined
                dense
              ></v-combobox>
              <v-combobox
                v-model="newGroup.cur_id"
                :items="courses"
                item-text="title"
                item-value="id"
                label="Courses"          
                outlined
                dense
              ></v-combobox>
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
                @click="addGroup"
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
                    :items="groups"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteGroup(item)"
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
            text: 'Name',
            align: 'start',
            sortable: false,
            value: 'gru_name',
          },
          
          { text: 'Teacher', sortable: false, value: 'tea_id'},
          { text: 'Course', sortable: false, value: 'cur_id' },
          {
            text: 'Created at',
            sortable: false,
            value: 'gru_created',
          },
          {
            text: 'Updated at',
            sortable: false,
            value: 'gru_updated',
          },
          {
            text: 'Actions',
            sortable: false,
            value: 'action',
          }
        ],
        groups: [],
        teachers: [],
        courses:[],
        users:[],
        // headers_courses: [{value:"cur_id"}],
        // headers_teachers: [{value:"tea_id"}],
        newGroup: {},
        URL: 'http://localhost:5000',
        config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
      }
    },
    methods: {
        addGroup() {
          var data = {
            gru_name:this.newGroup.gru_name,
            tea_id:this.newGroup.tea_id.id,
            cur_id:this.newGroup.cur_id.id,
          }
          axios.post(this.URL + '/create_group', data, this.config_request)
          .then((res) => {
            this.groups.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newGroup = {};
        },
        deleteGroup(item) {
          axios.delete(this.URL + '/delete_group/' + item.gru_id, this.config_request)
          .then((res) => {
            this.groups.splice(this.groups.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        },
        resetForm(){
          this.newGroup = {};
        }
    },
    created() {
        axios.get(this.URL + '/groups')
        .then((res) => { this.groups = res.data; })
        .catch((err) => { console.log(err); })

        axios.get(this.URL + '/users')
        .then((res) => { this.users = res.data; })
        .catch((err) => { console.log(err); })

        axios.get(this.URL + '/get_teacher_combobox')
        .then((res) => { this.teachers = res.data; })
        .catch((err) => { console.log(err); })

        axios.get(this.URL + '/get_course_combobox')
        .then((res) => { this.courses = res.data; })
        .catch((err) => { console.log(err); })
    },

    
  }
</script>