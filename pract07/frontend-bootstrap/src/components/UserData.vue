<template>
    <div>
        <h2>Users</h2>
      <b-table striped hover :items="users" :fields="fields"></b-table>
    </div>
  </template>
  
  <script>
// import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
// import VueAxios from 'vue-axios'
    export default {
      data() {
        return {
          // Note 'isActive' is left out and will not appear in the rendered table
          fields: [
            {
              key: 'usr_id',
              label: 'ID'
            },
            {
              key: 'usr_name',
              label: "Name"
            },
            {
              key: 'usr_last_name',
              label: 'Last Name'
            },
            {
              key: 'usr_dni',
              label: 'DNI'
            },
            {
                key: 'usr_email',
                label: 'Email'
            },
            {
                key: 'usr_passwd',
                label: 'Password'
            },
            {
                key: 'usr_dob',
                label: 'Day of Birth'
            },
            {
                key: 'usr_photo',
                label: 'Path to photo'
            }
          ],
          users: [],
          postURL: 'http://127.0.0.1:5000',
          config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        }
      },
      created(){
        axios.post(this.postURL + '/users')
            .then((res) => { this.users = res.data; })
            .catch((error) => { console.log(error) })
      }
    }
  </script>