<template>
	<div>

		<user-type-component/>

	</div>
</template>

<script>
	import UserTypeComponent from '@/components/UserTypeComponent.vue';
	
	export default {
		name: 'Testing',

		components: {
			UserTypeComponent,
		}
	}
</script>