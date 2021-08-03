from django.contrib import admin
from django.db import models
from django.contrib import admin
# Register your models here.


class TodoAdmin(models.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = 
