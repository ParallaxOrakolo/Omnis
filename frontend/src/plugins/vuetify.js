// eslint-disable-next-line semi, import/no-extraneous-dependencies
import '@mdi/font/css/materialdesignicons.css';
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconsfont: 'mdi',
  },
  // theme: {
  //   themes: {
  //     light: {
  //       primary: '#00f245',
  //       secondary: '#b0bec5',
  //       accent: '#8c9eff',
  //       error: '#b71c1c',
  //     },
  //     dark: {
  //       primary: '#00f245',
  //       secondary: '#b0bec5',
  //       accent: '#8c9eff',
  //       error: '#b71c1c',
  //     },
  //   },
  // },
});
