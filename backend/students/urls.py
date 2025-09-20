from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentProfileViewSet,
    AttendanceViewSet,
    TestResultViewSet,
    LeaveApplicationViewSet,
    StudyMaterialViewSet,
    TodoViewSet,
    TestViewSet,
    QuestionViewSet,
    NoticeViewSet,
    GalleryImageViewSet,
    PollViewSet,
    PollOptionViewSet,
    TimetableViewSet,
    FeePaymentViewSet,
    student_login,
    submit_test,
)

# Router for CRUD endpoints
router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet, basename="profiles")
router.register(r'attendance', AttendanceViewSet, basename="attendance")
router.register(r'results', TestResultViewSet, basename="results")
router.register(r'leaves', LeaveApplicationViewSet, basename="leaves")
router.register(r'study-materials', StudyMaterialViewSet, basename="study-materials")
router.register(r'todos', TodoViewSet, basename="todos")
router.register(r'tests', TestViewSet, basename="tests")
router.register(r'questions', QuestionViewSet, basename="questions")
router.register(r'notices', NoticeViewSet, basename="notices")
router.register(r'gallery', GalleryImageViewSet, basename="gallery")
router.register(r'polls', PollViewSet, basename="polls")
router.register(r'poll-options', PollOptionViewSet, basename="poll-options")
router.register(r'timetables', TimetableViewSet, basename="timetables")
router.register(r'fee-payments', FeePaymentViewSet, basename="fee-payments")

urlpatterns = [
    path("", include(router.urls)),

    # Custom routes
    path("auth/login/", student_login, name="student_login"),
    path("tests/<int:test_id>/submit/", submit_test, name="submit_test"),
]
