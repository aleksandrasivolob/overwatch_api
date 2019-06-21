from rest_framework import routers

from django.urls import include, path
from django.contrib import admin

from characters import views

router = routers.DefaultRouter()
router.register(r'characters', views.CharacterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
