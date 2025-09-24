from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import (
    StudentProfile, Attendance, Test, TestResult,
    LeaveApplication, StudyMaterial, Todo, Question,
    Notice, GalleryImage, Poll, PollOption, Timetable,
    FeePayment
)
from .serializers import (
    StudentProfileSerializer, AttendanceSerializer, TestSerializer, TestResultSerializer,
    LeaveApplicationSerializer, StudyMaterialSerializer, TodoSerializer, QuestionSerializer,
    NoticeSerializer, GalleryImageSerializer, PollSerializer, PollOptionSerializer,
    TimetableSerializer, FeePaymentSerializer
)


# --------------------
# ViewSets
# --------------------
class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    # Logged-in student → Get their own profile
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_profile(self, request):
        try:
            profile = StudentProfile.objects.get(user=request.user)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticated]

    # Custom endpoint → Submit marks
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        try:
            test = Test.objects.get(pk=pk)
            student_id = request.data.get("student_id")
            marks = int(request.data.get("marks"))

            if marks > test.total_marks:
                return Response({"error": "Marks cannot exceed total marks"},
                                status=status.HTTP_400_BAD_REQUEST)

            student = StudentProfile.objects.get(id=student_id)
            result, _ = TestResult.objects.get_or_create(student=student, test=test)
            result.marks_obtained = marks
            result.save()

            return Response({
                "message": "Test submitted successfully",
                "marks": result.marks_obtained,
                "total_marks": test.total_marks
            }, status=status.HTTP_200_OK)

        except (Test.DoesNotExist, StudentProfile.DoesNotExist):
            return Response({"error": "Invalid Test or Student"},
                            status=status.HTTP_404_NOT_FOUND)


class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated]


class StudyMaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]


class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticated]


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]


class PollOptionViewSet(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer
    permission_classes = [IsAuthenticated]


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticated]


class FeePaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer
    permission_classes = [IsAuthenticated]


# --------------------
# Custom API Endpoints
# --------------------
@api_view(["POST"])
def student_login(request):
    """
    Login using username & password → Returns auth token
    """
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successful",
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def submit_test(request, test_id):
    """
    Submit test marks for a student (outside ViewSet for flexibility)
    """
    try:
        test = Test.objects.get(id=test_id)
        student_id = request.data.get("student_id")
        marks = int(request.data.get("marks"))

        if marks > test.total_marks:
            return Response({"error": "Marks cannot exceed total marks"},
                            status=status.HTTP_400_BAD_REQUEST)

        student = StudentProfile.objects.get(id=student_id)
        result, _ = TestResult.objects.get_or_create(student=student, test=test)
        result.marks_obtained = marks
        result.save()

        return Response({
            "message": "Test submitted successfully",
            "student": student.user.username,
            "marks": marks,
            "total_marks": test.total_marks
        }, status=status.HTTP_200_OK)

    except (Test.DoesNotExist, StudentProfile.DoesNotExist):
        return Response({"error": "Invalid Test or Student"},
                        status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import random, string

@api_view(['POST'])
@permission_classes([AllowAny])   # 👈 override default IsAuthenticated
def student_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Invalid credentials"}, status=401)

    # Create or get token
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key,
        "username": user.username,
        "name": user.first_name,
        "user_id": user.id
    })