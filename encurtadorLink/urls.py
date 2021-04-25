from rest_framework.routers import DefaultRouter
from encurtadorLink.views import urlViewSet
from rest_framework.routers import DefaultRouter

from encurtadorLink.views import urlViewSet

router = DefaultRouter()
router.register(r'api', urlViewSet)
urlpatterns = router.urls

app_name = 'encurtadorLink'

