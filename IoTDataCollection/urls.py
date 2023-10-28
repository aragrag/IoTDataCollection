from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from iotapp.views import IoTObjectViewset, IoTDataViewset,\
    AdminIoTObjectViewset, AdminIoTDataViewset

from django.views.generic import TemplateView

router = routers.SimpleRouter()
router.register('objet', IoTObjectViewset, basename='objet')
router.register('data', IoTDataViewset, basename='data')

router.register('admin/objet', AdminIoTObjectViewset, basename='admin-objet')
router.register('admin/data', AdminIoTDataViewset, basename='admin-data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='base.html'), name='react_app'),
]