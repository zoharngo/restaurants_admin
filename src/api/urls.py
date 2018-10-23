
from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash = False)
router.register(r'api', views.RestaurantsViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
