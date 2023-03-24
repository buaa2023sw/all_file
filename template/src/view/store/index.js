import Vue from "vue"
import Vuex from 'vuex'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

//1.安装插件
Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        //当前用户账号
        username: window.localStorage.getItem('username'),
        userId: parseInt(window.localStorage.getItem('userId')),
        //登录状态
        loginStatus: !!window.localStorage.getItem('loginStatus'),
    },
    getters: {

    },
    //mutations只能以同步方式
    mutations: {
        getUser(state, username){
            console.log('username',username)
            state.username = username;
        },
        getLoginStatus(state, flag){
            state.loginStatus = flag;
        },
        editUserId(state,id){
            state.userId=id
            console.log('useridinjs',state.userId)
        }
    },
    actions: {

    }
});
export default store