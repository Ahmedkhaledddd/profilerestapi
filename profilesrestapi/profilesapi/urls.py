from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profilesapi import views
from . import views

router = DefaultRouter()
router.register('hello-veiwset', views.HelloViewSet , basename= 'hello-viewset')
router.register('profile-viewset', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
path('hello/',views.HelloAPIView.as_view(), name='hello-view'),
path('login/', views.UserLoginApiView.as_view()),
path('',include(router.urls)),
]
