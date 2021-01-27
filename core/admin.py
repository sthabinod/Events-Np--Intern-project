from django.contrib import admin
from .models import Contact, FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_display_links = ('question',)
    ordering = ['question']
    list_filter = ('question',)
    search_fields = ['question', 'answer']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'message', 'date')
    list_display_links = ('full_name', 'email')
    ordering = ['full_name']
    search_fields = ['full_name', 'email']
    list_filter = ('date',)