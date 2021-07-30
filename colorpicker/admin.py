from django.contrib import admin
from .models import Color

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'created_on', 'author')
    list_filter = ('title', 'color', 'created_on', 'author')
    # search_fields = ['title', 'color', 'author']
    search_fields = ['color']

admin.site.register(Color, ColorAdmin)