from django.urls import path, include

urlpatterns = [
    path('api/', include('doctores.urls')),
    path('api/', include('pacientes.urls')),
]