from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
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

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class StudyMaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollOptionViewSet(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class FeePaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer


# --------------------
# Custom API Endpoints
# --------------------
@api_view(["POST"])
def student_login(request):
    """
    Student login using username & password
    """
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        return Response({"message": "Login successful", "user_id": user.id})
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def submit_test(request, test_id):
    """
    Submit test result for a student
    """
    try:
        test = Test.objects.get(id=test_id)
        student_id = request.data.get("student_id")
        marks = request.data.get("marks")

        student = StudentProfile.objects.get(id=student_id)
        result, created = TestResult.objects.get_or_create(student=student, test=test)
        result.marks_obtained = marks
        result.save()

        return Response({"message": "Test submitted successfully", "marks": marks})
    except Test.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)
    except StudentProfile.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
