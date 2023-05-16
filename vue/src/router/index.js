import Vue from 'vue'
import Router from 'vue-router'
import websites from '../components/websites.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'websites',
      component: websites
    }
  ]
})
