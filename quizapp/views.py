from django.shortcuts import render
from quizapp.models import StudentDetails


def index(request):

    # sdetails = StudentDetails.objects.all()
    return render(request, "index.html")



