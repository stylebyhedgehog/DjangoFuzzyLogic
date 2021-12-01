
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('res', views.result, name='result'),
    path('admin', views.admin, name='admin'),
    path('adminsearch', views.admin_search, name='adm_search'),
    path('adminadd', views.admin_add, name='adm_add')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
