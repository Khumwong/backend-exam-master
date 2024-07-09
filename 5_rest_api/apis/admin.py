
from django.contrib import admin
from apis.models import School, Classroom, Teacher, Student

def delete_all(modeladmin, request, queryset):
    modeladmin.model.objects.all().delete()

delete_all.short_description = "Delete all records"

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    actions = [delete_all]

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    actions = [delete_all]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    actions = [delete_all]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = [delete_all]
