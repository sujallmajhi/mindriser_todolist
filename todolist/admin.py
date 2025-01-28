from django.contrib import admin
from .models import todolist

@admin.register(todolist)
class todolistAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Description', 'status']
    list_filter=['status']
    list_per_page=2
    list_editable=['status']
    search_fields=['Title']
