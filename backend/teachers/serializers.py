from rest_framework import serializers
from .models import TeacherProfile, TeachingPlan, PracticeQuestion, TeacherResponse


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = "__all__"


class TeachingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingPlan
        fields = "__all__"


class PracticeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeQuestion
        fields = "__all__"


class TeacherResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherResponse
        fields = "__all__"
