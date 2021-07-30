from django.views import generic
from .models import Color

class ColorList(generic.ListView):
    # queryset = Color.objects.filter(User).order_by('-created_on')
    queryset = Color.objects.all().order_by('-created_on')
    template_name = 'index.html'

