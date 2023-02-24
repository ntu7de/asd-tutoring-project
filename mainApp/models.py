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
    subject = models.CharField(max_length=100, default='')
    catalogNumber = models.CharField(max_length=100, default='')
    classSection = models.CharField(max_length=100, default='')
    classNumber = models.CharField(max_length=100, default='')
    className = models.CharField(max_length=100, default='')
    instructor = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.className

class TutorClasses(models.Model):
    tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    classID = models.ForeignKey(Classes, on_delete=models.CASCADE)
    rate = models.FloatField()

class TutorTime(models.Model):
    sessionID = models.AutoField(primary_key=True)
    tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
class SessionBooked(models.Model):
    sessionID = models.ForeignKey(TutorTime, on_delete=models.CASCADE)
    tstudentID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
