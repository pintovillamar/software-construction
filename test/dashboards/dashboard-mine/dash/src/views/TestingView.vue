<template>
	<div>
		<testing-componente/>

		<testing-componente2/>
	</div>
</template>

<script>
	import TestingComponente from '@/components/TestingComponente.vue';
	import TestingComponente2 from '@/components/TestingComponente2.vue';
	
	export default {
		name: 'Testing',

		components: {
			TestingComponente,
			TestingComponente2,
		}
	}
</script>