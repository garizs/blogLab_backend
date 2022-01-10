"""blogLab URL Configuration"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from backend.blog.posts import views as posts_views
from backend.blog.users import views as users_views
from backend.config import settings
from backend.core.handler404 import view_404

router = routers.SimpleRouter()
router.register(prefix=r'posts', viewset=posts_views.PostsViewSet)
router.register(prefix=r'users', viewset=users_views.UsersView, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("favicon.ico", RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
handler404 = view_404
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
