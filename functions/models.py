from django.db import models
 
class Internship(models.Model):
    name = models.CharField(max_length=100,unique=True)

class Applicants(models.Model):
    way=models.ForeignKey(Internship, on_delete = models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

class Body(models.Model):
    heading=models.ForeignKey(Internship, on_delete = models.CASCADE)
    deadline = models.DateTimeField()
    information = models.CharField(max_length=256)
    link=models.URLField()
