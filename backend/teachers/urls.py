from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherProfileViewSet,
    TeachingPlanViewSet,
    PracticeQuestionViewSet,
    TeacherResponseViewSet,
    LeaveManagementViewSet,
)

# Router for teacher APIs
router = DefaultRouter()
router.register(r'profiles', TeacherProfileViewSet, basename="teacher-profiles")
router.register(r'teaching-plans', TeachingPlanViewSet, basename="teaching-plans")
router.register(r'practice-questions', PracticeQuestionViewSet, basename="practice-questions")
router.register(r'responses', TeacherResponseViewSet, basename="responses")

# Special leave management routes
leave_management = LeaveManagementViewSet.as_view({
    "get": "list",
})

leave_approve = LeaveManagementViewSet.as_view({
    "post": "approve",
})

leave_reject = LeaveManagementViewSet.as_view({
    "post": "reject",
})

urlpatterns = [
    path("", include(router.urls)),

    # Extra leave endpoints
    path("leaves/", leave_management, name="teacher-leaves"),
    path("leaves/<int:pk>/approve/", leave_approve, name="approve-leave"),
    path("leaves/<int:pk>/reject/", leave_reject, name="reject-leave"),
]
