from django.urls import path
from django.urls import from django.conf import settings
from django.

app_name = 'blog'
urlpatterns = [
    path(''),
    path('<int:pk>')
]
