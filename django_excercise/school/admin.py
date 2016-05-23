from django.contrib import admin
from school.models import School, Classroom, Student

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','get_classroom',]

    def get_classroom(self, obj):
        return obj.classroom.name
    get_classroom.admin_order_field = 'classroom'
    get_classroom.short_description = 'classroom'


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name','get_students',] 

    def get_students(self, obj):
        students = Student.objects.filter(classroom=obj)
        return students.count()
    get_students.admin_order_field = 'students'
    get_students.short_description = 'Number of Students'

# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)
