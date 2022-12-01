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
                label="Tipo"
                required
              ></v-text-field>
              <v-text-field
                ref="tea_cat"
                v-model="newTeacher.tea_cat"
                label="Categoria"
                required
              ></v-text-field>
              <v-autocomplete
                ref="usr_name"
                :items="headers_user"
                v-model="newTeacher.usr_name"
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
                    <!--new---->

                    <template v-slot:item.actions="{ item }">
                      <div class="text-truncate">
                        <v-icon
                            small
                            class="mr-2"
                            @click="showEditDialog(item)"
                            color="blue" 
                          >
                            mdi-pencil
                        </v-icon>
                        <v-icon
                            small
                            @click="showDeleteDialog(item)"
                            color="pink" 
                          >
                            mdi-delete
                        </v-icon>
                      </div>
                    </template>

                    <!--new---->
                  </v-data-table>

                  <!-- Aquí empiezan los dialogs de UPDATE y DELETE -->

                <!-- Dialog para DELETE -->
                <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                      <v-card-title>Delete</v-card-title>
                      <v-card-text>
                        Are you sure you want to delete {{itemToDelete.tea_id}}?
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="dialogDelete = false">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="deleteTeacher(itemToDelete); dialogDelete = false">OK</v-btn>
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- Dialog para UPDATE -->
                <v-dialog v-model="dialog" max-width="500px">
                  <v-card>
                    <v-card-title>
                        <span editedItem.tea_id >Edit {{editedItem.tea_id}}</span>
                    </v-card-title>
                    <v-card-text>
                      <v-row>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.tea_id"
                            label="Profesor"
                            required
                          ></v-text-field>
                        </v-col>
                        <!-- <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.usr_id"
                            label="Usuario"
                            required
                          ></v-text-field>
                        </v-col> -->
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.tea_type"
                            label="Tipo"
                            required
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.tea_cat"
                            label="Categoria"
                            required
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="showEditDialog()">Cancel</v-btn>
                      <v-btn color="green " text @click="updateGroup(editedItem); showEditDialog()">Save</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <!--new---->

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
        //new
        dialog: false,
        dialogDelete: false,
        editedItem: {
          tea_id: '',
          usr_id: '',
          tea_type: '',
          tea_cat: '',
          tea_updated: '',
        },
        itemToDelete: {
          tea_id: '',
          usr_id: '',
          tea_type: '',
          tea_cat: '',
          tea_updated: '',
        },
        //new
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
          //new
          {
            text: 'Actions',
            value: 'actions',
            sortable: false
          }
          //new
        ],
        teachers: [],
        newTeacher: {},
        user:[],
        headers_user: [{value:"usr_name"}],
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
          axios.delete(this.URL + '/delete_teacher/' + item.tea_id, this.config_request)
          .then((res) => {
            this.teachers.splice(this.teachers.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        },
        //new
        updateTeacher(item) {
          axios.put(this.URL + '/update_teacher/' + item.tea_id, item, this.config_request)
          .then((res) => {
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        },
        showEditDialog(item) {
        this.editedItem = item||{}
        this.dialog = !this.dialog
        },
        showDeleteDialog(item) {
        this.itemToDelete = item
        this.dialogDelete = !this.dialogDelete
        },
        //new  
        resetForm(){
          this.newTeacher = {};
        }
    },
    //new
    clear () {
      this.newTeacher.tea_id = '';
      },
    //new
    created() {
        axios.get(this.URL + '/teachers')
        .then((res) => { this.teachers = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>