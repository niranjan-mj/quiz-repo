from django.db import models
<<<<<<< HEAD
=======
from django_countries.fields import CountryField
>>>>>>> 0c37f99a89e2e41ce4fda78d76daf0585f611725


class StudentDetails(models.Model):
    dob = models.DateField()
    email_id = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    score = models.IntegerField(max_length=2)
