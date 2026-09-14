from django.urls import path
from blog.views import home

from rest_framework.routers import DefaultRouter
from blog.viewsets import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', home, name='home'),
] + router.urls