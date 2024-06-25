from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from . import settings  
from django.conf.urls.static import static

urlpatterns = [
    path("", include("django.conf.urls.i18n")),
    path('',include('authentication.urls')),
    path('',include('app.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

