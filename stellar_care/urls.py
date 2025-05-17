from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from records import api_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()
router.register(r'patients', api_views.PatientViewSet, basename='patient')

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Allauth authentication
    path('accounts/', include('allauth.urls')), 

    # App-specific
    path('records/', include('records.urls')),
    path('', RedirectView.as_view(url='/records/', permanent=False)),

    # API Routes
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc', SpectacularRedocView.as_view(), name='redoc'),
]