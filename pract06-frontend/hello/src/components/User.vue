<template>
    <div class="user">
        <!-- <h2>Usuario</h2>
        <ul class="myUL">
            <li v-for="user in users">
                {{ user.name }} - {{ user.email }}
                <button type="button" v-on:click="deleteUser(user)">x</button>
            </li>
        </ul> -->

        <h2>Usuario</h2>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Email</th>
                    <th>Dia de nacimiento</th>
                    <th>DNI</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in users">
                    <td>{{ user.usr_name }}</td>
                    <td>{{ user.usr_last_name }}</td>
                    <td>{{ user.usr_email }}</td>
                    <td>{{ user.usr_dob }}</td>
                    <td>{{ user.usr_dni }}</td>
                    <td>
                        <button type="button" v-on:click="deleteUser(user)">x</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <br/>
        <form v-on:submit="addUser">
            <input type="text" v-model="newUser.name" placeHolder="name">
            <input type="text" v-model="newUser.email" placeHolder="email">
            <button type="Submit">Add</button>
        </form>
    </div>
</template>

<script>
     export default{    
        data(){ 
            return {
            // users: [
            //     { name: 'Jose', email: 'jose@ulasalle.edu.pe', contacted: false },
            //     { name: 'Yoshiro', email: 'yoshiro@ulasalle.edu.pe', contacted: false }
            // ],
            users: [],
            newUser: {}
            }
        },
        methods:{
            addUser(e){
                e.preventDefault();
                console.log("user added")
                this.users.push(this.newUser)
                this.newUser = {};
            },
            deleteUser(user){
                this.users.splice(this.users.indexOf(user),1)

                console.log("user deleted")
            }
        },
        created(){
                this.$http.post('http://localhost:5000/users').then(res => this.users = res.body);
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