# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView # type: ignore
from rest_framework import permissions
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title="Pupils API",
        description="Pupils registration app",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='asliddinberdiyevv@gmail.com'),
        license=openapi.License(name='Pupils registration app license')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('groups.urls')),  # Groups API
    path('api/v1/', include('pupils.urls')),  # Pupils API
    path('auth/login/', TokenObtainPairView.as_view(), name='jwt-create'),  # JWT Login
    path('auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),  # JWT Refresh
    path('auth/logout/', TokenBlacklistView.as_view(), name='jwt-logout'),  # JWT Logout
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
