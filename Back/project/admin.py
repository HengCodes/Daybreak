from django.contrib import admin

from .models import Project


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


admin.site.site_header = "DayBreak后台管理"
admin.site.site_title = 'DayBreak后台管理'
admin.site.register(Project)
