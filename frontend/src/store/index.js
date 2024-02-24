import { createStore } from 'vuex'
export default createStore ( {
    state: {
        isAuthorized: true,
        organizations: [
            {
                name: "name 1",
                countTasks: 2,
                countMembers: 1,
                description: "4243",
                members: [
                  {
                    name: 'Иванов Василий',
                    email: 'example@mail.ru',
                    telNum: '8900123-45-67',
                    countTask: 0,
                    countProjects: 0,
                    rating: 1,
                    
                  },
                  {
                    name: 'Иванов Иван',
                    email: 'example@mail.ru',
                    telNum: '8900123-45-67',
                    countTask: 0,
                    countProjects: 0,
                    rating: 1
                  }
                ],
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
                description: "3334",
                countTasks: 20,
                countMembers: 2,
                members: [
                  {
                    name: 'Иванов Иван',
                    email: 'example@mail.ru',
                    telNum: '8900123-45-67',
                    countTask: 0,
                    countProjects: 0,
                    rating: 1
                  },
                  {
                    name: 'Иванов Иван',
                    email: 'example@mail.ru',
                    telNum: '8900123-45-67',
                    countTask: 0,
                    countProjects: 0,
                    rating: 1
                  }
                ],
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
        pushOrganization(state, newOrganization) {
            state.organizations.push(newOrganization)
            console.log('sef');
        },

    },
    actions: {

    }
})