from django.urls import path
from profilesapi import views
from . import views

urlpatterns = [
path('hello/',views.HelloAPIView.as_view(), name='hello-view'),
]
