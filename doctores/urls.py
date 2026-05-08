from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctores', DoctorViewSet)

urlpatterns = [path('', include(router.urls))]