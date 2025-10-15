from django.contrib import admin
from .models import Class,Student,Subject,Guardian,AcademicClass,Exam ,Grading,Result


class ClassAdmin(admin.ModelAdmin):
    list_display = ("class_s","class_short_form")

class StudentAdmin(admin.ModelAdmin):
    list_display =("first_name","second_name","class_s")

class SubjectAdmin (admin.ModelAdmin):
    list_display = ("subject","subject_short_form")
class GuardianAdmin (admin.ModelAdmin):
    list_display= ("first_name","second_name","relationship","student")

class AcademicClassAdmin(admin.ModelAdmin):
    list_display = ("class_s","status","year")

class ExamAdmin(admin.ModelAdmin):
    list_display =("exam_type","subject","exam_date","status")

class GradingAdmin(admin.ModelAdmin):
    list_display = ("points","max_score","min_score","grade")

class ResultAdmin (admin.ModelAdmin):
    list_display = ("student","exam","score","grade")


admin.site.register(Class,ClassAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Guardian,GuardianAdmin)
admin.site.register(AcademicClass,AcademicClassAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Grading,GradingAdmin)
admin.site.register(Result,ResultAdmin)


# Register your models here.
