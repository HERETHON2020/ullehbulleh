from django.shortcuts import render
from .models import info

# Create your views here.
def create(request) :
    info.picture = request.FILES['picture']

def as_view(request):
    return render(request, 'blog.html')