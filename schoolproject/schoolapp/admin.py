from django.contrib import admin
from .models import Department, Material, Student, Course

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Material)
admin.site.register(Course)