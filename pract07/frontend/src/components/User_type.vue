<template>
    <div class="user_type">
        <h2> Roles </h2>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th> ID </th>
                    <th>Nombre</th>
                    <th>Acciones</th>
                </tr>
            </thead>
                <tbody>
                    <tr v-for="user_type in user_types">
                        <td>{{user_type.ust_id}}</td>
                        <td>{{ user_type.ust_name }}</td>
                        <td>
                        <button type="button" v-on:click="deleteUser_Type(user_type)">x</button>
                        </td>
                    </tr>
                </tbody>
        </table>
        <br>
        <form v-on:submit="addUser_Type">
            <input type="text" v-model="newUser_type.ust_name" placeHolder="Rol">
            <button type="submit"> Add </button>
        </form>
        <br>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){ 
        return { 
            user_types: [],
            newUser_type: {},
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }           
        }
    },
    methods:{
        addUser_Type(){ 
            axios.post(this.postURL + '/create_user_type', this.newUser_type, this.config_request)
                .then(res => {                                         
                    this.user_types.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });
            console.log("fin");
            this.newUser_type = {};
        },
        deleteUser_Type(user_type){                      
            axios.post(this.postURL + '/delete_user_type/' + user_type.ust_id , {}, this.config_request)
                .then(res => {                      
                    this.user_types.splice(this.user_types.indexOf(user_type), 1);                    
                })
                .catch((error) => {
                    console.log(error)
                });  
        }
    },
    created(){ 
        axios.post(this.postURL + '/user_types')
            .then((res) => { this.user_types = res.data; })
            .catch((error) => { console.log(error) })
    }
}    
</script>

<style>
    .user_type {
        background-color: gray;
    }
    .myUL{
        display: inline-block;
        text-align: center;
    }
    .myTable{
        display: inline-block;
        text-align: center;
    }
    table, th, td {
        width: 100%;
        border: 1px solid;
        border-collapse: collapse;
    }
</style>