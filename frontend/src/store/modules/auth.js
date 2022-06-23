/* eslint-disable no-shadow */
import { REGISTER_USER, AUTHENTICATED_USER, AUTHENTICATE_USER } from '@/graphql';
import { apolloClient } from '@/vue-apollo';

import Vue from 'vue';

const state = {
  user: {},
  authStatus: false,
  token: localStorage.getItem('apollo-token') || null,
};

const getters = {
  user: (state) => state.user,
  isAuth: (state) => !!state.token,
  authStatus: (state) => state.authStatus,
};

const actions = {
  async loginUser({ dispatch }, userData) {
    try {
      const {
        data: { authenticateUser },
      } = await apolloClient.query({
        query: AUTHENTICATE_USER,
        variables: userData,
      });
      dispatch('setUserData', authenticateUser);
    } catch (error) {
      Vue.prototype.$alertFeedback('alerts.loginFail', 'error', error);
    }
  },

  // eslint-disable-next-line no-unused-vars
  async registerUser({ dispatch }, userData) {
    console.log(apolloClient);
    const {
      data: { registerUser },
    } = await apolloClient.mutate({
      mutation: REGISTER_USER,
      variables: userData,
    });
    dispatch('setUserData', registerUser);
  },

  async setUserData({ commit }, payload) {
    commit('LOGIN_USER', payload);
    commit('SET_TOKEN', payload);

    // set token in localstorage
    localStorage.setItem('apollo-token', payload.token);
    // localStorage.setItem('apollo-token', payload.token.split(' ')[1]);
  },
  async getAuthUser({ commit, dispatch }) {
    try {
      const {
        data: { authUserProfile },
      } = await apolloClient.query({
        query: AUTHENTICATED_USER,
      });
      commit('LOGIN_USER', { user: authUserProfile });
    } catch (error) {
      dispatch('logoutUser');
    }
  },
  logoutUser({ commit }) {
    commit('LOGOUT_USER');
  },
};

const mutations = {
  LOGIN_USER(state, payload) {
    state.user = payload.user;
    state.authStatus = true;
  },
  SET_TOKEN(state, payload) {
    state.token = payload;
  },
  LOGOUT_USER(state) {
    state.user = {};
    state.authStatus = false;
    state.token = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true,
};