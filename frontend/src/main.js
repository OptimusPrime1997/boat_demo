// // The Vue build version to load with the `import` command
// // (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from 'vue'
// import App from './App'
// import router from './router'
//
//
// Vue.config.productionTip = false
//
// import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
// Vue.use(ElementUI);
//
// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import axios from 'axios'

import VueRouter from 'vue-router'
import routes from './routes'
axios.defaults.withCredentials=true

import VueAxios from 'vue-axios'

Vue.use(VueAxios,axios);

Vue.use(ElementUI)
Vue.use(VueRouter)
// Vue.use(axios)
// Vue.prototype.$axios=axios

const router = new VueRouter({
  routes
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
