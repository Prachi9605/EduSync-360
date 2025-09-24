from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentProfileViewSet, AttendanceViewSet, TestViewSet, TestResultViewSet,
    LeaveApplicationViewSet, StudyMaterialViewSet, TodoViewSet, QuestionViewSet,
    NoticeViewSet, GalleryImageViewSet, PollViewSet, PollOptionViewSet,
    TimetableViewSet, FeePaymentViewSet,
    student_login, submit_test, register_student   # ✅ import new view
)

router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test-results', TestResultViewSet)
router.register(r'leave-applications', LeaveApplicationViewSet)
router.register(r'study-materials', StudyMaterialViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'gallery', GalleryImageViewSet)
router.register(r'polls', PollViewSet)
router.register(r'poll-options', PollOptionViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'fees', FeePaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student_login/', student_login, name='student_login'),
    path('tests/<int:test_id>/submit/', submit_test, name="submit_test"),
    path('register_student/', register_student, name="register_student"),  # ✅ new route
]
