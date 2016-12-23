from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework import routers
from apps.main import urls as main_urls


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^', include(main_urls)),
]
  