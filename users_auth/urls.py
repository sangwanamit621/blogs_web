from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUserViewSet, ChangePasswordViewSet, MyTokenObtainPairViewSet,UpdateUserDetailsViewSet

app_name = 'users-auth'

urlpatterns = [
    path("token/",MyTokenObtainPairViewSet.as_view(),name="token_generate"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("register/",RegisterUserViewSet.as_view(),name="user_register"),
    path("change_password/<str:username>/", ChangePasswordViewSet.as_view(), name="change_user_password"),
    path("update_details/<str:username>/",UpdateUserDetailsViewSet.as_view(),name="update_user_details")
]