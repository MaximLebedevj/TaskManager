from django.urls import include, path

from .views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('profile/', UserApiView.as_view()),
    path('profile/edit/', UpdateApiProfile.as_view()),
    path('organization/create', CreateApiOrganization.as_view()),
    path('organization/', ShowAllOrganizationsApi.as_view()),
    path('organization/<int:organization_pk>/', OrganizationApiView.as_view()),
    path('organization/<int:organization_pk>/project/create', CreateProjectApi.as_view())
]
