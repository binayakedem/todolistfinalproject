from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('name','mission','startDate','isCompleted',)
    list_filter=('isCompleted',)
    search_fields=('name',)
    list_editable=()
  
    