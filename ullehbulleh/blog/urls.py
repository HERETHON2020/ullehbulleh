from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('',예시),
    path('<int:pk>')
]
