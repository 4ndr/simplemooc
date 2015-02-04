from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):#modifica o admin do site
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)
