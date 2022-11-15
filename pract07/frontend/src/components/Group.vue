<template>
    <div class="group">
        <h2> Grupos </h2>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th> ID </th>
                    <th>Nombre</th>
                    <th>Profesor</th>
                    <th>Curso</th>
                </tr>
            </thead>
                <tbody>
                    <tr v-for="group in groups">
                        <td>{{group.gru_id}}</td>
                        <td>{{ group.gru_name}}</td>
                        <td>{{ group.tea_id }}</td>
                        <td>{{ group.cur_id}}</td>
                        <td>
                        <button type="button" v-on:click="deleteGroup(group)">x</button>
                        </td>
                    </tr>
                </tbody>
        </table>
        <br>
        <form v-on:submit="addGroup()">
            <input type="text" v-model="newGroup.gru_name" placeHolder="Nombre">
            <input type="text" v-model="newGroup.tea_id" placeHolder="Teacher">
            <input type="text" v-model="newGroup.cur_id" placeHolder="Curso">
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
            groups: [],
            newGroup: {},
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }           
        }
    },
    methods:{
        addGroup(){ 
            axios.post(this.postURL + '/create_group', this.newGroup, this.config_request)
                .then(res => {                                         
                    this.groups.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });
            console.log("fin");
            this.newGroup = {};
        },
        deleteGroup(group){                      
            axios.post(this.postURL + '/delete_group/' + group.gru_id , {}, this.config_request)
                .then(res => {                      
                    this.groups.splice(this.groups.indexOf(group), 1);                    
                })
                .catch((error) => {
                    console.log(error)
                });  
        }
    },
    created(){ 
        axios.post(this.postURL + '/groups')
            .then((res) => { this.groups = res.data; })
            .catch((error) => { console.log(error) })
    }
}    
</script>

<style>
    .group {
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