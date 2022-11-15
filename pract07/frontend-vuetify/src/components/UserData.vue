<template>
    <div>
        <h2 class="users">Users</h2>
        <v-data-table
            :headers="headers"
            :items="users"
            :items-per-page="3"
            class="elevation-1"
        ></v-data-table>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    data() {
        return {
            headers: [
                {
                    value: 'usr_id',
                    text: 'ID'
                },
                {
                    value: 'usr_name',
                    text: "Name"
                },
                {
                    value: 'usr_last_name',
                    text: 'Last Name'
                },
                {
                    value: 'usr_dni',
                    text: 'DNI'
                },
                {
                    value: 'usr_email',
                    text: 'Email'
                },
                {
                    value: 'usr_passwd',
                    text: 'Password'
                },
                {
                    value: 'usr_dob',
                    text: 'Day of Birth'
                }
            ],
            users: [],
            postURL: 'http://localhost:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    },
    created(){
        axios.post(this.postURL + '/users')
            .then((res) => { this.users = res.data; })
            .catch((err) => { console.log(err); })
    }
}

</script>

<style>
    .users {
        text-align: center;
    }
</style>