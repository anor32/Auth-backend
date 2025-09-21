from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterUserApi, UserLoginApi,UserProfileApi,UserLogout,DeleteUser,AdminManageRoles

app_name = UsersConfig.name
urlpatterns = [
    path('register/', RegisterUserApi.as_view(), name='user_register'),
    path('login/', UserLoginApi.as_view(), name='user_login'),
    path('profile/', UserProfileApi.as_view(), name='user_profile'),
    path('profile/<int:pk>/', UserProfileApi.as_view(), name='user_profile_detail'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('delete/<int:pk>/', DeleteUser.as_view(), name='user_delete'),
    path('admin/manage_roles/', AdminManageRoles.as_view(), name='admin_manage_roles'),
]