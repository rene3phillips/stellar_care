from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('records/', include('records.urls')),
    path('', RedirectView.as_view(url='/records/', permanent=False)),
]