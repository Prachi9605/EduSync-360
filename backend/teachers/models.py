from django.db import models
from django.conf import settings


# ✅ Teacher Profile (main model)
class TeacherProfile(models.Model):
    user = models.OneToOneField(   # one teacher = one user
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile"
    )
    full_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)   # e.g., Mathematics, Physics
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.subject})"


# ✅ Weekly Teaching Plan (syllabus updates)
class TeachingPlan(models.Model):
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="teaching_plans"
    )
    week_start = models.DateField()
    week_end = models.DateField()
    syllabus_details = models.TextField()  # JSON/text of topics
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.full_name} | {self.week_start} - {self.week_end}"


# ✅ Practice Questions (posted by teachers for revision)
class PracticeQuestion(models.Model):
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="practice_questions"
    )
    subject = models.CharField(max_length=100)
    question_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.teacher.full_name}"


# ✅ Teacher Responses to Student Doubts
class TeacherResponse(models.Model):
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="responses"
    )
    student = models.ForeignKey(   # 🔑 no direct import → use string reference
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="teacher_responses"
    )
    question_text = models.TextField()
    answer_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.teacher.full_name} to {self.student.user.username}"
