from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

app_name = 'blogs-app'

router = DefaultRouter()
router.register("posts",PostViewSet,basename="post-ops")
router.register("comments",CommentViewSet,basename="comment-ops")

urlpatterns = [
    path("",include(router.urls))
]