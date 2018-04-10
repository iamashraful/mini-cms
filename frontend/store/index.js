import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex);

const state = {
    count: 0,
    loginDetails: {},
    isAuthenticated: localStorage.getItem("auth") === "true",
    appLogo: "",
    token: localStorage.getItem("token") || "",
    pages: [
        {id: 1, name: 'Test Page', path: 'test-page'},
    ]
};

export default new Vuex.Store({
    state,
    actions,
    mutations,
})
