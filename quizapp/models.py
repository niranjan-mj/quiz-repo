from django.db import models


class StudentDetails(models.Model):
    dob = models.DateField(blank=False)
    email_id = models.EmailField(max_length=254, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    score = models.IntegerField(max_length=2,null=True)
