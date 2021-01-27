from django.contrib import admin
from .models import Blog



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'date_added', 'date_edited')
    search_fields = ['title', 'content']
    list_display_links = ('title',)
    list_filter = ('date_added',)
    ordering = ['title']

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"