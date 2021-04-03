from django.contrib import admin
from .models import *


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name',)
    list_display_links = ('id', 'school_name',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_name')


class WeekdayAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LessonTimeAdmin(admin.ModelAdmin):
    list_display = ('time',)


class AudienceAdmin(admin.ModelAdmin):
    list_display = ('audience', 'school_name')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_last_name', 'teacher_first_name', 'teacher_middle_name', 'school_name')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('s_class', 'weekday', 'lesson_time', 'lesson', 'audience', 'teacher', 'school')
    list_display_links = ('s_class', 'weekday', 'lesson_time', 'lesson', 'audience', 'teacher')


admin.site.register(School, SchoolAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Weekday, WeekdayAdmin)
admin.site.register(LessonTime, LessonTimeAdmin)
admin.site.register(Audience, AudienceAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Schedule, ScheduleAdmin)
