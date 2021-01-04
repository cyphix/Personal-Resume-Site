from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views



app_name = 'interactive_resume'

urlpatterns = [
    path('', views.interactive_resume_view, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
