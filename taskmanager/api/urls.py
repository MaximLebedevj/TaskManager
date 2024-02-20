from django.urls import include, path

from .views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('profile/', UserApiView.as_view()),
    path('profile/edit/', UpdateApiProfile.as_view()),
    path('organization/', CreateApiOrganization.as_view()),
    path('organization/<int:organization_pk>', OrganizationChangeAPI.as_view()),
    # path('organization/<int:organization_pk>/add_parts', OrganizationAddParticipantAPI.as_view()),
]
