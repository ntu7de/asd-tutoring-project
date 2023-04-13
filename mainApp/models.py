from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models



TimeSelections = (
    ("Select Time", "Select Time"),
    ("9:00 AM", "9:00 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10:00 AM", "10:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11:00 AM", "11:00 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12:00 PM", "12:00 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1:00 PM", "1:00 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2:00 PM", "2:00 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3:00 PM", "3:00 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4:00 PM", "4:00 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5:00 PM", "5:00 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    email = models.EmailField()
    pronouns = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    tutor_or_student = models.CharField(max_length=100, default="tutor")
    fun_fact = models.CharField(max_length=200)
#
# class Tutor(models.Model): #tutor profile!
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
#     monday_start = models.TimeField()
#     monday_end = models.TimeField()
#     tuesday_start = models.TimeField()
#     tuesday_end = models.TimeField()
#     wednesday_start = models.TimeField()
#     wednesday_end = models.TimeField()
#     thursday_start = models.TimeField()
#     thursday_end = models.TimeField()
#     friday_start = models.TimeField()
#     friday_end = models.TimeField()
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    monday_start = models.CharField(max_length=100, null=True, blank=True)
    monday_end = models.CharField(max_length=100, null=True, blank=True)
    tuesday_start = models.CharField(max_length=100, null=True, blank=True)
    tuesday_end = models.CharField(max_length=100, null=True, blank=True)
    wednesday_start = models.CharField(max_length=100, null=True, blank=True)
    wednesday_end = models.CharField(max_length=100, null=True, blank=True)
    thursday_start = models.CharField(max_length=100, null=True, blank=True)
    thursday_end = models.CharField(max_length=100, null=True, blank=True)
    friday_start = models.CharField(max_length=100, null=True, blank=True)
    friday_end = models.CharField(max_length=100, null=True, blank=True)
    # def clean(self):
    #     super().clean()
    #
    #     # Check if end time is later than start time for each day
    #     if self.monday_start >= self.monday_end:
    #         raise ValidationError("Monday end time must be later than start time.")
    #     if self.tuesday_start >= self.tuesday_end:
    #         raise ValidationError("Tuesday end time must be later than start time.")
    #     if self.wednesday_start >= self.wednesday_end:
    #         raise ValidationError("Wednesday end time must be later than start time.")
    #     if self.thursday_start >= self.thursday_end:
    #         raise ValidationError("Thursday end time must be later than start time.")
    #     if self.friday_start >= self.friday_end:
    #         raise ValidationError("Friday end time must be later than start time.")
    # # monday_hours = models.CharField(max_length=200)
    # tuesday_hours = models.CharField(max_length=200)
    # wednesday_hours = models.CharField(max_length=200)
    # thursday_hours = models.CharField(max_length=200)
    # friday_hours = models.CharField(max_length=200)
    # classes = models.CharField(max_length=200)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.CharField(max_length=200)


class Classes(models.Model):
    # classID = models.AutoField(primary_key=True, null = False)
    # classID = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default='')
    catalognumber = models.CharField(max_length=100, default='')
    classsection = models.CharField(max_length=100, default='')
    classnumber = models.CharField(max_length=100, default='', primary_key= True, unique= True)
    classname = models.CharField(max_length=100, default='')
    instructor = models.CharField(max_length=200, default='')
    body = models.TextField(default='')
    def __str__(self):
        return self.classname

class tutorClasses(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

class Request(models.Model):
        startTime = models.CharField(max_length=100, null=True, blank=True)
        endTime = models.CharField(max_length=100, null=True, blank=True)
        location = models.CharField(max_length=100, null=True, blank=True)
        tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
        student = models.ForeignKey(User, on_delete=models.CASCADE)
        approved = models.CharField(max_length=100, null=True, blank=True)
        date = models.CharField(max_length=100, null=True, blank=True)

# class TutorClasses(models.Model):
#     tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
#     classID = models.ForeignKey(Classes, on_delete=models.CASCADE)
#     rate = models.FloatField()
#
#
# # class TutorTime(models.Model):
# #     sessionID = models.AutoField(primary_key=True)
# #     tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
# #     day = models.CharField(max_length=20)
# #     start_time = models.TimeField()
# #     end_time = models.TimeField()
# #     location = models.CharField(max_length=100)
# #
# #
# # class SessionBooked(models.Model):
# #     sessionID = models.ForeignKey(TutorTime, on_delete=models.CASCADE)
# #     tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
# #     studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
