// import { constants } from "fs";
import Vue from 'vue';
import Vuex from 'vuex';

// import modules
import node from './modules/node';
import alert from './modules/alert';
import auth from './modules/auth';
import controls from './modules/controls';

// import serverJson from "@/engine/data/json/config/editable/server.json";
Vue.use(Vuex);

const store = new Vuex.Store({
  // estado do dado
  modules: {
    node,
    alert,
    auth,
    controls,
  },
});
export { store };
