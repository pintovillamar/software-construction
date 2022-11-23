<template>
	<div>
		<testing-componente/>

		<testing-componente2/>

		<testing-component3/>
	</div>
</template>

<script>
	import TestingComponente from '@/components/TestingComponente.vue';
	import TestingComponente2 from '@/components/TestingComponente2.vue';
	import TestingComponent3 from '@/components/TestingComponent3.vue';
	
	export default {
		name: 'Testing',

		components: {
			TestingComponente,
			TestingComponente2,
			TestingComponent3,
		}
	}
</script>