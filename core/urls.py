from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, TripViewSet, InstagramViewSet,TripImageViewSet,DestinationInfoView

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'trips', TripViewSet)
router.register(r'instagram', InstagramViewSet)
router.register(r'trip-images', TripImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('destination-info/', DestinationInfoView.as_view(), name='destination-info'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
