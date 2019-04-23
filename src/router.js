import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const router = new Router({
 // mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/',
      name: 'home',
      component: () => import('./components/Home.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./components/LoginForm.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./components/RegisterForm.vue')
    },
      {
      path: '/test',
      name: 'test',
      component: () => import('./components/test.vue'),
      meta: {
                requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录
    },
    },
    {
      path: '*',
      name: 'notfound',
      component: () => import('./components/NotFound.vue'),

    }]
});


router.beforeEach((to, from, next) => {
     console.log(to)
    if (!!to.meta.requireAuth) { // 判断该路由是否需要登录权限
            if ( !!localStorage.token) { // 判断缓存里面是否有 userName  //在登录的时候设置它的值
                console.log('yes')
                next();
            } else {
                next({
                    path: '/login',
                    query: {
                        redirect: to.fullPath
                    } // 将跳转的路由path作为参数，登录成功后跳转到该路由
                })
            }
        } else {
            next();

        }
});


export default router;