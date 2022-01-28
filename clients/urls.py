from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='clients')


urlpatterns = [
    path('clients/read/', views.read_csv),
    path('', include(router.urls))
]