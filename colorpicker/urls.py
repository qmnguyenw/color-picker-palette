from . import views
from django.urls import path

urlpatterns = [
    path('', views.ColorList.as_view(), name='home'),
    # path('', views.ColorList, name='home'),
]