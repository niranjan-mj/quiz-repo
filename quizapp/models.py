from django.db import models

class StudentDetails(models.Model):
    dob = models.DateField()
    email_id = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    score = models.IntegerField(max_length=2)
