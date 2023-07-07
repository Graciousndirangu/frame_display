from django.contrib import admin
from .models import URL

# Register your models here.
class URLAdmin(admin.ModelAdmin):
    list_display = ('frame', 'url', 'duration', 'duration_unit')
    list_filter = ('frame', 'duration_unit')
    search_fields = ('frame__name', 'url')

admin.site.register(URL, URLAdmin)
