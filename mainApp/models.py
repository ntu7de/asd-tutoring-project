from django.contrib.auth.models import User
from django.db import models


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

class Tutor(models.Model): #tutor profile!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    monday_hours = models.CharField(max_length=200)
    tuesday_hours = models.CharField(max_length=200)
    wednesday_hours = models.CharField(max_length=200)
    thursday_hours = models.CharField(max_length=200)
    friday_hours = models.CharField(max_length=200)
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

    def __str__(self):
        return self.classname

class tutorClasses(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

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
