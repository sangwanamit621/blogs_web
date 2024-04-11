from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/",include("blogs_app.urls",namespace='blogs-app')),
    path("users/",include("users_auth.urls",namespace='users-auth'))
]
