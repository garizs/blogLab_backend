"""blogLab URL Configuration"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers

from apps.curators import views as curators_views
from apps.posts import views as posts_views
from apps.auth import views as auth
from apps.users import views as user_views
from config import settings
from apps.core.handler404 import view_404

router = routers.SimpleRouter()
router.register(prefix=r'posts', viewset=posts_views.PostsViewSet)
router.register(prefix=r'auth', viewset=auth.UsersView, basename='auth')
router.register(prefix=r'curators', viewset=curators_views.CuratorsViewSet, basename='curators')
router.register(prefix=r'users', viewset=user_views.UsersView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', auth.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', auth.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path("favicon.ico", RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
handler404 = view_404
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
