import { createStore } from 'vuex'
export default createStore ( {
    state: {
        isAuthorized: true,
        organizations: [
            {
                name: "name 1",
                countTasks: 2,
                countMembers: 1,
                tasks: [
                    {
                      title: "sfesfsef",
                      deadline: "25 февраля 2024",
                      countMembers: 5,
                      countTasks: 43,
                    },
                    {
                      title: "sfsef",
                      deadline: "25 февраля 2024",
                      countMembers: 5,
                      countTasks: 43,
                    },
                  ],
            },
            {
                name: "name 2",
                countTasks: 20,
                countMembers: 2,
                tasks: [
                    {
                      title: "hkuhk",
                      deadline: "25 февраля 2024",
                      countMembers: 5,
                      countTasks: 43,
                    },
                    {
                      title: "kh",
                      deadline: "26 февраля 2024",
                      countMembers: 2,
                      countTasks: 4,
                    },
                  ],
        
            },
        ]

    },
    getters: {
    //   getTasksByName(state, nameOrganization) {
    //     // const organization = state.organizations.map(organization => organization.name == nameOrganization);
    //     return nameOrganization
    // }
    getTasksByName: (state) => (nameOrganization) => {
      const selectOrganization = state.organizations.find(organization =>organization.name === nameOrganization)

      return selectOrganization
    }
    },
    mutations: {
        pushOrganization(state) {
            state.organizations.push(organization)
        },

    },
    actions: {

    }
})