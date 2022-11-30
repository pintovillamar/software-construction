<template>
	<div>
		<testing-componente/>

		<testing-componente2/>

		<testing-component3/>

		<testing-component4/>

		<TestingComponent5/>

		<TestingComponent6/>

		<TestingComponent7/>
	</div>
</template>

<script>
	import TestingComponente from '@/components/TestingComponente.vue';
	import TestingComponente2 from '@/components/TestingComponente2.vue';
	import TestingComponent3 from '@/components/TestingComponent3.vue';
	import TestingComponent4 from '@/components/TestingComponent4.vue';
	import TestingComponent5 from '@/components/TestingComponent5.vue';
	import TestingComponent6 from '@/components/TestingComponent6.vue';
	import TestingComponent7 from '@/components/TestingComponent7.vue';
	
	export default {
		name: 'Testing',

		components: {
    TestingComponente,
    TestingComponente2,
    TestingComponent3,
    TestingComponent4,
    TestingComponent5,
    TestingComponent6,
	TestingComponent7
}
	}
</script>