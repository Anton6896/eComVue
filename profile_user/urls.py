from django.urls import path
from .views import profile_home_view

app_name = 'profile'

urlpatterns = [
    path('', profile_home_view, name='home')
]
