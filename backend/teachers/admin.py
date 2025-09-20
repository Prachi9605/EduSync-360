from django.contrib import admin
from .models import TeacherProfile, PracticeQuestion, TeacherResponse, TeachingPlan

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "department")

@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "created_on")
    search_fields = ("subject",)

@admin.register(TeacherResponse)
class TeacherResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "teacher", "get_question")  # fixed

    def get_question(self, obj):
        return obj.question.question_text if obj.question else "-"
    get_question.short_description = "Question"

@admin.register(TeachingPlan)
class TeachingPlanAdmin(admin.ModelAdmin):
    list_display = ("id", "teacher", "week_start", "week_end")
