import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const $api = axios.create({
    baseURL: '/api/v1'
})

$api.interceptors.request.use(
    (config) => {
        let token = localStorage.getItem('token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

const $auth = axios.create({
    baseURL: '/auth'
})

const state = {
    token: null,
    loading: false,
    error: '',
    user: null
}

const mutations = {
    SET_TOKEN(state, token) {
        state.token = token
    },
    SET_USER(state, user) {
        state.user = user
    },
    LOADING_PENDING(state) {
        state.loading = true
    },
    LOADING_SUCCESS(state) {
        state.loading = false
        state.error = ''
    },
    LOADING_ERROR(state, error) {
        state.loading = false
        state.error = error
    }
}

const actions = {
    login({
        commit
    }, userInfo) {
        commit('LOADING_PENDING')
        return $api.post('/oauth/token', userInfo).then((res) => {
            localStorage.setItem('token', res.data.access_token)
            commit('SET_TOKEN', res.data.access_token)
            commit('LOADING_SUCCESS')
        }).catch((err) => {
            const error = err.response.data.message
            commit('LOADING_ERROR', error)
        })
    },
    register({
        commit
    }, userInfo) {
        commit('LOADING_PENDING')
        return $auth.post('/register', userInfo).then((res) => {
            commit('LOADING_SUCCESS')
        }).catch((err) => {
            const error = err.response.data.message
            commit('LOADING_ERROR', error)
        })
    },
    loadUser({
        commit
    }, token) {
        commit('SET_TOKEN', token)
        return $api.get('/user').then((res) => {
            commit('SET_USER', res.data)
        })
    },
    logout({
        commit
    }) {
        localStorage.removeItem('token');
        commit('SET_USER', null);
        commit('SET_TOKEN', null);
    }
}

const getters = {
    token: state => state.token,
    loading: state => state.loading,
    error: state => state.error,
    user: state => state.user
}

const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})

export default store;