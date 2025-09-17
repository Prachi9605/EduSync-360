from rest_framework import serializers
from .models import *

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = "__all__"

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = "__all__"

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = "__all__"

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = "__all__"

class FeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePayment
        fields = "__all__"
