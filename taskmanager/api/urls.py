from django.urls import include, path

from .views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('profile/', UserApiView.as_view()),
    path('profile/edit/', UpdateApiProfile.as_view()),
    path('organization/', CreateOrganizatonApi.as_view()),
    path('organization/<int:organization_pk>/', ShowAllAndUpdateOrganizationApi.as_view()),
    path('organization/<int:organization_pk>/project/create', CreateProjectApi.as_view())
]
