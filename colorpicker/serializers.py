from rest_framework import fields, serializers
from .models import Color
from django.contrib.auth.models import User

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'title', 'color', 'created_on', 'author')