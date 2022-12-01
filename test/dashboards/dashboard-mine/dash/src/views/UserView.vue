<template>
	<div>

		<user-component/>

	</div>
</template>

<script>
	import UserComponent from '@/components/UserComponent.vue';
	
	export default {
		name: 'Testing',

		components: {
			UserComponent,
		}
	}
</script>