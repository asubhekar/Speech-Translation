from django.urls import path
from .views import sp_translation, home

urlpatterns = [
    path('api/', sp_translation.as_view(), name='API Endpoint'),
    path('', home, name = 'Home')
]