from django.shortcuts import render
from quizapp.models import StudentDetails
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    sdetails = StudentDetails.objects.all()
    if request.method == "POST":

        print('start1', request.method)
        return HttpResponseRedirect("register_redirect.html")

    return render(request, "index.html")






