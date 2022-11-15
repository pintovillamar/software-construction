<template>
    <div>
        <h2>Groups</h2>
      <b-table striped hover :items="groups" :fields="fields"></b-table>
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
              key: 'gru_id',
              label: 'Group ID'
            },
            {
              key: 'gru_name',
              label: "Group Name"
            },
            {
              key: 'tea_id',
              label: 'Teacher ID'
            },
            {
              key: 'cur_id',
              label: 'Course ID'
            }
          ],
          groups: [],
          postURL: 'http://127.0.0.1:5000',
          config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        }
      },
      created(){
        axios.post(this.postURL + '/groups')
            .then((res) => { this.groups = res.data; })
            .catch((error) => { console.log(error) })
      }
    }
  </script>