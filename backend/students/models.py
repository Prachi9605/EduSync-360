from django.db import models
from django.contrib.auth.models import User


# 1. Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    roll_no = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()  # e.g. 1,2,3,4
    course = models.CharField(max_length=100)
    skills = models.TextField(blank=True, null=True)  # store as comma-separated or JSON
    dob = models.DateField()
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    fee_status = models.CharField(
        max_length=20,
        choices=[("PAID", "Paid"), ("PENDING", "Pending"), ("PARTIAL", "Partial")],
        default="PENDING"
    )

    def __str__(self):
        return f"{self.user.username} ({self.roll_no})"


# 2. Attendance
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("PRESENT", "Present"), ("ABSENT", "Absent")],
        default="PRESENT"
    )

    class Meta:
        unique_together = ("student", "date")  # prevent duplicate entries

    def __str__(self):
        return f"{self.student.roll_no} - {self.date} - {self.status}"


# 3. Test
class Test(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, blank=True, null=True)
    total_marks = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.subject} - {self.topic or 'General'}"


# 4. Test Result
class TestResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="test_results")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="results")
    marks_obtained = models.IntegerField()
    rank = models.IntegerField(blank=True, null=True)  # calculated after submission
    analysis = models.TextField(blank=True, null=True)  # e.g. strengths/weaknesses

    class Meta:
        unique_together = ("student", "test")

    def __str__(self):
        return f"{self.student.roll_no} - {self.test.subject} ({self.marks_obtained})"


# 5. Leave Application
class LeaveApplication(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="leave_applications")
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("PENDING", "Pending"), ("APPROVED", "Approved"), ("REJECTED", "Rejected")],
        default="PENDING"
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave {self.student.roll_no} ({self.status})"


# 6. Study Material
class StudyMaterial(models.Model):
    subject = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to="study_materials/")
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.file.name}"


# 7. Todo
class Todo(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="todos")
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.roll_no} - {self.task[:20]}"

# 1. Ask Seniors (Q&A / DM)
class Question(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="questions")
    senior = models.ForeignKey(User, on_delete=models.CASCADE, related_name="senior_responses")  # target senior
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    asked_on = models.DateTimeField(auto_now_add=True)
    answered_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Q by {self.student.roll_no} → {self.senior.username}"


# 2. Notice Board
class Notice(models.Model):
    NOTICE_TYPE = [
        ("CLASS", "Class"),
        ("COLLEGE", "College"),
    ]
    title = models.CharField(max_length=200)
    message = models.TextField()
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPE, default="CLASS")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notice_type} Notice: {self.title}"


# 3. Gallery
class GalleryImage(models.Model):
    event_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="gallery/")
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} - {self.caption or ''}"


# 4. Poll / Voting System
class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=255)
    votes = models.ManyToManyField(StudentProfile, blank=True, related_name="voted_options")

    def __str__(self):
        return f"{self.option_text} ({self.poll.question})"


# 5. Timetable
class Timetable(models.Model):
    branch = models.CharField(max_length=100)
    year = models.IntegerField()
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("MON", "Monday"), ("TUE", "Tuesday"), ("WED", "Wednesday"),
            ("THU", "Thursday"), ("FRI", "Friday"), ("SAT", "Saturday")
        ]
    )
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch} Y{self.year} - {self.subject} ({self.day_of_week})"


# 6. Fee Payment (Optional: history tracking)
class FeePayment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="fee_payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[("PAID", "Paid"), ("PENDING", "Pending"), ("PARTIAL", "Partial")],
        default="PENDING"
    )
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.roll_no} - {self.status} ({self.amount})"


# 🔹 Extra fields for Student Profile Showcase
StudentProfile.add_to_class("github", models.URLField(blank=True, null=True))
StudentProfile.add_to_class("projects", models.TextField(blank=True, null=True))