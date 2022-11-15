<template>
    <div class="user">
        <h2>Usuario</h2>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>DNI</th>
                    <th>Email</th>
                    <th>Dia de nacimiento</th>
                    <th>Foto</th>
                    <th>Acciones</th>
                </tr>
            </thead>
                <tbody>
                    <tr v-for="user in users">
                        <td> {{ user.usr_id}}</td>
                        <td>{{ user.usr_name }}</td>
                        <td>{{ user.usr_last_name }}</td>
                        <td> {{user.usr_dni}} </td>
                        <td>{{ user.usr_email }}</td>
                        <td> {{ user.usr_passwd }}</td>
                        <td>{{ user.usr_dob }}</td>
                        <!-- <td>{{ user.usr_photo }}</td> -->
                        <!-- <td>
                            <img v-bind:src="`${user.usr_photo}`">
                        </td> -->
                        <td >{{user.usr_photo}}</td>
                        <td>
                            <button type="button" v-on:click="deleteUser(user)">x</button>
                        </td>
                    </tr>
            </tbody>
        </table>
        <br/>
        <form v-on:submit="addUser">
            <input type="text" v-model="newUser.usr_name" placeHolder="Nombre">
            <input type="text" v-model="newUser.usr_last_name" placeHolder="Apellido">
            <input type="text" v-model="newUser.usr_dni" placeHolder="DNI">
            <input type="text" v-model="newUser.usr_email" placeHolder="Email">
            <input type="text" v-model="newUser.usr_passwd" placeHolder="Contraseña">
            <input type="text" v-model="newUser.usr_dob" placeHolder="Dia de nacimiento">
            <input type="text" v-model="newUser.usr_photo" placeHolder="Foto">
            <button type="Submit">Agregar</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    data(){ 
        return {
            image: '',
            fields: [],
            users: [],
            newUser: {"ust_id":2},
            postURL: 'http://localhost:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            }
        }
    },
    methods:{
        addUser(){
            axios.post(this.postURL + '/create_user', this.newUser, this.config_request)
                .then(res => {
                    this.users.push(res.data);
                    console.log(res.data);
                })
                .catch(error => {
                    console.log(error);
                });
            console.log("user added");
            this.newUser = {};
            },
            deleteUser(user){
                axios.post(this.postURL + '/delete_user/' + user.usr_id, {}, this.config_request)
                .then(res => {
                    this.users.splice(this.users.indexOf(user), 1);
                })
                .catch((error) => {
                    console.log(error);
                });
                console.log("user deleted");
            }
        },
    created(){ 
        axios.post(this.postURL + '/users')
            .then((res) => { this.users = res.data; })
            .catch((error) => { console.log(error) })
        }
    }
</script>

<style>
    .user {
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