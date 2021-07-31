from django.views import generic
from .models import Color
from rest_framework import viewsets, status

class ColorList(generic.ListView):
# class ColorList(viewsets.ModelViewSet):
    # queryset = Color.objects.filter(User).order_by('-created_on')
    queryset = Color.objects.all().order_by('-created_on')
    template_name = 'index.html'

