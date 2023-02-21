from django.db import models
class Tutor(models.Model):
    tstudentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField()
    pronouns = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    fun_fact = models.CharField(max_length=200)
class Student(models.Model):
    studentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField()
    pronouns = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    fun_fact = models.CharField(max_length=200)
class Classes(models.Model):
    classID = models.IntegerField(primary_key=True)
    className = models.CharField(max_length=100)

class TutorClasses(models.Model):
    tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    classID = models.ForeignKey(Classes, on_delete=models.CASCADE)
    rate = models.FloatField()
# Create your models here.
