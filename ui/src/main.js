import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import moment from 'moment';
import axios from 'axios';

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://localhost:8000/api';
Object.defineProperty(Vue.prototype, '$moment', {value: moment});
Object.defineProperty(Vue.prototype, '$axios', {value: axios});

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
