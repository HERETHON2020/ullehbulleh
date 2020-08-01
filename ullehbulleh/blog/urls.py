from django.urls import path
from django.conf import settings
import blog.views

app_name = 'blog'
urlpatterns = [
    path('',blog.views.as_view,name="index"),
    # path('<int:pk>')
]
