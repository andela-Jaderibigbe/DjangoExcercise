from django.contrib import admin
from school.models import School, Classroom, Student

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'classroom',) 

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name',) 

# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)
