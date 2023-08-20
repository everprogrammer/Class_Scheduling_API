from django.contrib import admin
from .models import Course, Professor, Classroom, TimeSlot

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    pass

class ProfessorAdmin(admin.ModelAdmin):
    pass

class ClassroomAdmin(admin.ModelAdmin):
    pass

class TimeSlotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)


