import { createStore } from 'vuex'
export default createStore ( {
    state: {
        isAuthorized: true,
        organizations: [
            {
                name: "Зимняя проектная школа",
                countTasks: 2,
                countMembers: 2,
                description: "Lorem ipsum dolor sit amet consectetur. Id turpis metus et adipiscing adipiscing tincidunt venenatis pharetra feugiat. Mauris et quam et vel cursus quam vestibulum. Venenatis lorem nisl hac nulla. Porttitor feugiat faucibus sodales arcu pretium. Urna neque nisl maecenas a faucibus nisl at auctor et. Suspendisse viverra pretium velit morbi augue feugiat.",
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
                      title: "task 1",
                      deadline: "25 февраля 2024",
                      countMembers: 5,
                      countTasks: 43,
                    },
                    {
                      title: "task 1",
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
                      title: "task 1",
                      deadline: "25 февраля 2024",
                      countMembers: 5,
                      countTasks: 43,
                    },
                    {
                      title: "task 2",
                      deadline: "26 февраля 2024",
                      countMembers: 2,
                      countTasks: 4,
                    },
                  ],
        
            },
        ]

    },
    getters: {
      getTasksByName: (state) => (nameOrganization) => {
        const selectOrganization = state.organizations.find(organization =>organization.name === nameOrganization)

        return selectOrganization
      }
    },
    mutations: {
        pushOrganization(state, newOrganization) {
            state.organizations.push(newOrganization)
        },

    },
    actions: {

    }
})