import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            component: () => import('@/view/login.vue'),
            children:[
                {
            path: '/login/:loginStatus',
            meta: {
                title: '登录注册'
            },
            component: (resolve) => require(['../view/login.vue'], resolve)
        }
            ]
        },
        {
            path: '/user',
            component: () => import('@/view/user/user'),
            children: [
                {
                    path : '',
                    meta: {
                        title: '用户主页'
                    },
                    component: () => import('@/view/user/user_home')
                },
                {
                    path : 'userHome',
                    meta: {
                        title: '用户主页'
                    },
                    component: () => import('@/view/user/user_home')
                },
                {
                    path: 'userDetail',
                    meta: {
                        title: '个人中心'
                    },
                    component: (resolve) => require(['../view/user/user_information'], resolve)
                },
                {
                    path: '*',
                    meta: {
                        title: '已为登录状态'
                    },
                    redirect: '/login/login',
                    //component: (resolve) => require(['../components/customer/login'], resolve)
                    component: (resolve) => require(['../view/user/user_home'], resolve)
                },
            ]
        },
    ],
    mode: "hash" // 去除访问时候带#问题
})

