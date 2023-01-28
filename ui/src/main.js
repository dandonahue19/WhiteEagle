import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import moment from 'moment';
import axios from 'axios';

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://ec2-3-94-180-253.compute-1.amazonaws.com:8000/0/api';
Object.defineProperty(Vue.prototype, '$moment', {value: moment});
Object.defineProperty(Vue.prototype, '$axios', {value: axios});

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
