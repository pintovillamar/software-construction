<!-- Templates HTML -->
<template>
    <div class="methods_component">
        <h2> {{ title }}</h2>
        Usuario: {{ user.name }} <br />

    <button type="button" v-on:click="saludar(user.name)">Call a method</button> <br />

    Binded to user.name
    <input type="text" v-model="user.name"> <br />

    Keyup event:
    <input type="text" v-on:keyup="typing"> <br />

    Keyup ENTER event:
    <input type="text" v-on:keyup.enter="typingEnter"> <br />

    </div>
</template>
    
    <!-- Scripts JavaScript -->
<script>
    export default{    
        data(){ 
            return {
                title: 'Eventos en Vue',
                user: {id: 1, name: 'Jose', lastname: 'Pinto'}
            }
        },
        methods:{
            saludar(text){
                console.log(text)
            },
            typing(e){
                // console.log(e);
                if (e.target.value == 'quit'){
                    console.log('exit ...')
                }
            },
            typingEnter(e){
                console.log('ENTER')
            }
        }
    }
</script>
    
    <!-- Styles CSS -->
<style>
    .methods_component{
        background-color: gray;
    }
</style>