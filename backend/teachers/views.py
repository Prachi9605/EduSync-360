from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import TeacherProfile, TeachingPlan, PracticeQuestion, TeacherResponse
from .serializers import (
    TeacherProfileSerializer,
    TeachingPlanSerializer,
    PracticeQuestionSerializer,
    TeacherResponseSerializer,
)
from students.models import LeaveApplication, StudentProfile
from students.serializers import LeaveApplicationSerializer


# ✅ Teacher Profile CRUD
class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer


# ✅ Weekly Teaching Plan CRUD
class TeachingPlanViewSet(viewsets.ModelViewSet):
    queryset = TeachingPlan.objects.all()
    serializer_class = TeachingPlanSerializer


# ✅ Practice Questions CRUD
class PracticeQuestionViewSet(viewsets.ModelViewSet):
    queryset = PracticeQuestion.objects.all()
    serializer_class = PracticeQuestionSerializer


# ✅ Teacher Responses CRUD
class TeacherResponseViewSet(viewsets.ModelViewSet):
    queryset = TeacherResponse.objects.all()
    serializer_class = TeacherResponseSerializer


# ✅ Special Case: Manage student leaves (Approve/Reject)
class LeaveManagementViewSet(viewsets.ViewSet):
    """
    Teachers can approve/reject student leave applications
    """

    def list(self, request):
        leaves = LeaveApplication.objects.all()
        serializer = LeaveApplicationSerializer(leaves, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        leave = get_object_or_404(LeaveApplication, pk=pk)
        leave.status = "approved"
        leave.save()
        return Response({"status": "Leave Approved ✅"})

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        leave = get_object_or_404(LeaveApplication, pk=pk)
        leave.status = "rejected"
        leave.save()
        return Response({"status": "Leave Rejected ❌"})
