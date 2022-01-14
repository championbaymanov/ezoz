from django.contrib import admin

from request.models import *


class RequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'approved']
    list_filter = ['approved']
    search_fields = ['full_name']
    date_hierarchy = 'created_at'
    ordering = ['created_at']


admin.site.register(RequestModel, RequestAdmin)