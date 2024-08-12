from django.urls import path
from .views import homepage_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage_view, name='homepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
