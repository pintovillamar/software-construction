<!-- Templates HTML -->
<template>
<div class='simple_component'>
    <h2>This is a component</h2> 
    my_var: {{ my_var }}
    my_var2: {{ my_var2 }}     
</div>
</template>

<!-- Scripts JavaScript -->
<script>
export default{    
    data(){ 
        return {
            my_var: 'Hello',
            my_var2: 'World'            
        }
    }
}
</script>

<!-- Styles CSS -->
<style>
    .simple_component{
        background-color: gray;
    }
</style>