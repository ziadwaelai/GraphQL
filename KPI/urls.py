from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KPIViewSet

# Set up the router for the KPI viewset
router = DefaultRouter()
router.register(r'kpi', KPIViewSet, basename='kpi')

# Define the URL patterns for the KPI app
urlpatterns = [
    path('', include(router.urls)),
]
