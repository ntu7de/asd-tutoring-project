from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField()
    pronouns = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    is_tutor = models.BooleanField(null=False, blank=False, default=False)
    is_student = models.BooleanField(null=False, blank=False, default=False)
    fun_fact = models.CharField(max_length=200)

class Tutor(models.Model): #tutor profile!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.IntegerField()
    classes = models.CharField(max_length=200)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.CharField(max_length=200)

class TutorDB(models.Model):
    # id = models.AutoField(primary_key=True)
    # user = models.ManyToOneRel(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToManyField(User, on_delete=models.CASCADE)
    catalogNumber = models.CharField(max_length=100, default='')
    rate = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)

class Classes(models.Model):
    # classID = models.AutoField(primary_key=True, null = False)
    # classID = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, default='')
    catalogNumber = models.CharField(max_length=100, default='', primary_key= True)
    classSection = models.CharField(max_length=100, default='')
    classNumber = models.CharField(max_length=100, default='')
    className = models.CharField(max_length=100, default='')
    instructor = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.className


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
