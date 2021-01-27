from django.contrib import admin
from .models import Category, Organiser, Person, Program, Schedule, Speaker,Event,File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ['name']}
    ordering = ['name']
    search_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date', 'venue', 'organiser', 'person', 'date_added')
    search_fields = ['title']
    list_filter = ('start_date', 'end_date', 'date_added')
    ordering = ['title']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['category', 'organiser', 'person']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'event')
    raw_id_fields = ['event']


@admin.register(Organiser)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website', 'date_added')
    search_fields = ['name', 'email']
    ordering = ['name']
    list_filter = ('date_added', 'date_edited')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ['full_name']
    ordering = ['full_name']


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'link')
    ordering = ['name']
    search_fields = ['name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title']
    ordering = ['date']
    raw_id_fields = ['program']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'speaker')
    search_fields = ['title']
    list_filter = ('time',)
    ordering = ['title']
    raw_id_fields = ['speaker']