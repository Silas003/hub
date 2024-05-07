from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=[
        'student','supervised_by','year','link']
    search_fields=['year','student','supervised_by']
    list_filter=['year']