import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainView.vue'
import OrganizationsView from '../views/OrganizationsView.vue'
import RegistrationView from '../views/RegistrationView.vue'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: OrganizationsView
        },
        {
            path: '/Organizations',
            component: OrganizationsView
        },
        {
            path: '/Registration',
            component: RegistrationView
        },
    ]
})

export default router