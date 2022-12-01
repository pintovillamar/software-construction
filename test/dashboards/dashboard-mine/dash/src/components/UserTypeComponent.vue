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
                
                label="Rol"
                required
              ></v-text-field>
              <v-text-field
                ref="ust_desc"
                v-model="newUserType.ust_desc"
                
                label="Descripción"
                required
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn text>
                Clear
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
                  </v-data-table>
                  <!--new---->


                  <!-- Aquí empiezan los dialogs de UPDATE y DELETE -->


                <!-- Dialog para DELETE -->
                <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                      <v-card-title>Delete</v-card-title>
                      <v-card-text>
                        Are you sure you want to delete {{itemToDelete.ust_name}}?
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="dialogDelete = false">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="deleteUserType(itemToDelete); dialogDelete = false">OK</v-btn>
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- Dialog para UPDATE -->
                <v-dialog v-model="dialog" max-width="500px">
                  <v-card>
                    <v-card-title>
                        <span editedItem.ust_name >Edit {{editedItem.ust_name}}</span>
                    </v-card-title>
                    <v-card-text>
                      <v-row>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.ust_name"
                            label="Rol"
                            required
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.ust_desc"
                            label="Descripción"
                            required
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="showEditDialog()">Cancel</v-btn>
                      <v-btn color="green " text @click="updateUserType(editedItem); showEditDialog()">Save</v-btn>
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
          ust_id: '',
          ust_name: '',
          ust_desc: '',
          ust_updated: '',
        },
        itemToDelete: {
          ust_id: '',
          ust_name: '',
          ust_desc: '',
          ust_updated: '',
        },
        //new
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
          //new
          {
            text: 'Actions',
            value: 'actions',
            sortable: false
          }
          //new
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
        },
        //new
        updateUserType(item) {
          axios.put(this.URL + '/update_user_type/' + item.ust_id, item, this.config_request)
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
        resetForm() {
          this.newUserType = {};
        }
        
    },
    //new
    clear () {
      this.newUserType.ust_name = '';
      },
    //new
    created() {
        axios.get(this.URL + '/user_types')
        .then((res) => { this.user_types = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>