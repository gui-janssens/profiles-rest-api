from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

#registing routers for viewSets
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) #does not need base_name because UserProfileViewSet has a QuerySet

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
