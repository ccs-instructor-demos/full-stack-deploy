
from rest_framework.routers import DefaultRouter

from .views import PlanetViewSet


router = DefaultRouter()
router.register(r'planets', PlanetViewSet, base_name='planet')

urlpatterns = router.urls