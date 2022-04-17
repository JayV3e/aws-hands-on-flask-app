import Vue from 'vue';
import VueRouter from 'vue-router';
import Thankful from '../components/Thankful.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Thankful,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
