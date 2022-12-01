import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/InicioView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/TestingView.vue')
  },
  {
    path: '/face',
    name: 'face',
    component: () => import('../views/FaceView.vue')
  },
  {
    path: '/user',
    name: 'user',
    component: () => import('../views/UserView.vue')
  },
  {
    path: '/group',
    name: 'group',
    component: () => import('../views/GroupView.vue')
  },
  {
    path: '/course',
    name: 'course',
    component: () => import('../views/CourseView.vue')
  },
  {
    path: '/teacher',
    name: 'teacher',
    component: () => import('../views/TeacherView.vue')
  },
  {
    path: '/enroll',
    name: 'enroll',
    component: () => import('../views/EnrollView.vue')
  },
  {
    path: '/schedule',
    name: 'schedule',
    component: () => import('../views/ScheduleView.vue')
  },
  {
    path: '/roles',
    name: 'roles',
    component: () => import('../views/RolesView.vue')
  }
  
]

const router = new VueRouter({
  routes
})

export default router
