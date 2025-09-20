from django.contrib import admin
from .models import (
    StudentProfile, Attendance, Test, TestResult,
    LeaveApplication, StudyMaterial, Todo, Question,
    Notice, GalleryImage, Poll, PollOption, Timetable,
    FeePayment
)


# 1. Student Profile
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'course', 'year', 'branch', 'fee_status')
    search_fields = ('user__username', 'roll_no', 'course', 'branch')
    list_filter = ('branch', 'year', 'fee_status')


# 2. Attendance
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student__roll_no', 'student__user__username')
    list_filter = ('status', 'date')


# 3. Test
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'total_marks', 'date')
    search_fields = ('subject', 'topic')
    list_filter = ('date',)


# 4. Test Result
@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test', 'marks_obtained', 'rank')
    search_fields = ('student__roll_no', 'test__subject')
    list_filter = ('test',)


# 5. Leave Application
@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'reason', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date')
    search_fields = ('student__roll_no', 'reason')


# 6. Study Material
@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('subject', 'uploaded_by', 'uploaded_on')
    list_filter = ('uploaded_on',)
    search_fields = ('subject',)


# 7. Todo
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('student', 'task', 'is_completed', 'created_on')
    list_filter = ('is_completed',)
    search_fields = ('student__roll_no', 'task')


# 8. Question (Ask Seniors)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('student', 'senior', 'question_text', 'answer_text', 'asked_on')
    search_fields = ('student__roll_no', 'senior__username', 'question_text')


# 9. Notice
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_type', 'created_on')
    list_filter = ('notice_type',)
    search_fields = ('title', 'message')


# 10. Gallery
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'caption', 'uploaded_by', 'uploaded_on')
    search_fields = ('event_name', 'caption')
    list_filter = ('uploaded_on',)


# 11. Poll
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_by', 'created_on')
    search_fields = ('question',)


# 12. PollOption
@admin.register(PollOption)
class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option_text')
    search_fields = ('poll__question', 'option_text')


# 13. Timetable
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('branch', 'year', 'day_of_week', 'subject', 'start_time', 'end_time', 'faculty')
    list_filter = ('branch', 'year', 'day_of_week')
    search_fields = ('subject', 'faculty')


# 14. Fee Payment
@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'payment_date')
    search_fields = ('student__roll_no',)
