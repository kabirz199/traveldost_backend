from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, TripViewSet, InstagramViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'trips', TripViewSet)
router.register(r'instagram', InstagramViewSet)

urlpatterns = [
    path('', include(router.urls)),
]