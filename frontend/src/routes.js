import Login from './views/Login.vue'
import Detail from './views/detail.vue'
import Table from './views/table.vue'
// import Homeinx from './views/homeinx.vue'

let routes = [
    {
        path: '/Login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/detail',
        component: Detail,
        name: '',
        hidden: true
    },
    {
        path: '/table',
        component: Table,
        name: '',
        hidden: true
    },
    // {
    //     path: '/homeinx',
    //     component: homeinx,
    //     name: '',
    //     hidden: true
    // },

];

export default routes;
