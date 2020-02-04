import Vue from 'vue'
import Router from 'vue-router'
import Current from '@/components/Current'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Current',
      component: Current
    }
  ]
})
