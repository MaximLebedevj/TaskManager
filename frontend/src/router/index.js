import { createRouter, createWebHistory } from 'vue-router'
import OrganizationsView from '../views/OrganizationsView.vue'
import OrganizationView from '../views/OrganizationView.vue'

import RegistrationView from '../views/RegistrationView.vue'
import TaskView from '../views/TaskView.vue'


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
        {
            path: '/Organizations/:nameOrganization',
            component: OrganizationView
        },
        {
            path: '/Organizations/:nameOrganization/:nameTask',
            component: TaskView
        },
    ]
})

export default router
