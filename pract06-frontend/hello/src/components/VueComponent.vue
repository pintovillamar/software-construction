<!-- Templates HTML -->
<template>
    <div class="simple_component">
        <h2>This is a component</h2> 
        Nombre: {{ user.name }} <br />
        Nombre Completo: {{ fullname }} <br /> 
        Mensaje de App.vue: {{ msg }} <br />
        ID: {{ user.id }} <br />

        <div v-if='showname'>
            <p>showName == true</p>
        </div>

        <div v-else='showname'>
            <p>showName == false</p>
        </div>

        <ul>
            <li v-for='task in tasks'>
                {{ task.title }}
            </li>
        </ul>
        
    </div>
</template>
    
    <!-- Scripts JavaScript -->
<script>
    export default{    
        data(){ 
            return {
                title: 'Construccion de Software',
                user: {id: 2, name: 'Juan', lastname: 'Perez'},
                showname: true,
                tasks: [{title: 'eat', des: 'eat food'},{title: 'sleep', des: 'sleep 8 hours'}]
            }
        },
        computed: {
            fullname(){
                return this.user.name + ' ' + this.user.lastname;
            },
            getid(){
                return this.user.id;
            }
        },
        // Props to pass arguments
        props: {
            msg: { type: String, default: 'default' }
        }
    }
</script>
    
    <!-- Styles CSS -->
<style>
    .simple_component{
        background-color: gray;
    }
</style>