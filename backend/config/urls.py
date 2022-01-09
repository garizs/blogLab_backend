"""blogLab URL Configuration"""

from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import routers
from backend.blog.posts import views as posts_views
from backend.config import settings
from backend.core.handler404 import view_404
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(prefix=r'posts', viewset=posts_views.PostsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
handler404 = view_404
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

