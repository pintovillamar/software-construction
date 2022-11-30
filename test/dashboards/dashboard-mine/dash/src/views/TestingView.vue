<template>
	<div>
		<user-type-component/>

		<user-component/>

		<group-component/>

		<course-component/>

		<teacher-component/>

		<enroll-component/>

		<schedule-component/>
	</div>
</template>

<script>
	import UserTypeComponent from '@/components/UserTypeComponent.vue';
	import UserComponent from '@/components/UserComponent.vue';
	import GroupComponent from '@/components/GroupComponent.vue';
	import CourseComponent from '@/components/CourseComponent.vue';
	import TeacherComponent from '@/components/TeacherComponent.vue';
	import EnrollComponent from '@/components/EnrollComponent.vue';
	import ScheduleComponent from '@/components/ScheduleComponent.vue';
	
	export default {
		name: 'Testing',

		components: {
			UserTypeComponent,
			UserComponent,
			GroupComponent,
			CourseComponent,
			TeacherComponent,
			EnrollComponent,
			ScheduleComponent
		}
	}
</script>