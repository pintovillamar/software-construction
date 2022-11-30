<template>
    <v-container>
        <v-row class="text-center" >
            <v-col>
                <h1>Tabla Schedule</h1>
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
                ref="sch_begin"
                v-model="newSchedule.sch_begin"
                :rules="[() => !!name || 'This field is required']"
                :error-messages="errorMessages"
                label="Begin"
                required
              ></v-text-field>
              <v-text-field
                ref="sch_end"
                v-model="newSchedule.sch_end"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="End"
                required
              ></v-text-field>
              <v-text-field
                ref="sch_day"
                v-model="newSchedule.sch_day"
                :rules="[() => !!description || 'This field is required']"
                :error-messages="errorMessages"
                label="Day"
                required
              ></v-text-field>
              <v-text-field
                ref="gru_id"
                v-model="newSchedule.gru_id"
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
                @click="addSchedule"
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
                    Tabla Schedule
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
                    :items="schedules"
                    :search="search"
                    >
                    <template v-slot:item.action="{item}">
                      <v-btn
                      class="mx-0"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="deleteSchedule(item)"
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
            value: 'sch_begin',
          },
          { text: 'Description', sortable: false, value: 'sch_end' },
          { text: 'Description', sortable: false, value: 'sch_day' },
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
        schedules: [],
        newSchedule: {},
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
        addSchedule() {
          axios.post(this.URL + '/create_schedule', this.newSchedule, this.config_request)
          .then((res) => {
            this.schedules.push(res.data);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
          this.newSchedule = {};
        },
        deleteSchedule(item) {
          axios.delete(this.URL + '/delete_schedule/' + item.sch_id, this.config_request)
          .then((res) => {
            this.schedules.splice(this.schedules.indexOf(item), 1);
            console.log(res.data)
          })
          .catch((err) => { console.log(err); })
        }
    },
    created() {
        axios.get(this.URL + '/schedules')
        .then((res) => { this.schedules = res.data; })
        .catch((err) => { console.log(err); })
    },
    
  }
</script>