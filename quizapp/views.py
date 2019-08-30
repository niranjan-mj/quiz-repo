from django.shortcuts import render, redirect
from quizapp.models import StudentDetails


def index(request):
    sdetails = StudentDetails.objects.all()
    if request.method == "POST":
        bool = False
        data1 = ''
        data2 = ''
        data3 = ''
        data4 = ''
        print(request.POST,'post check')
        if "submit" in request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email_id = request.POST['email_id']
            dob = request.POST['dob']

            if first_name == '':
                bool = True
                data1 = {'status': 'false', 'message_1': 'Enter the first_name pls'}

            if last_name == '':
                bool = True
                data2 = {'status': 'false', 'message_2': 'Enter the last_name pls'}

            if email_id == '':
                bool = True
                data3 = {'status': 'false', 'message_3': 'Enter the email_id pls'}

            if dob == '':
                bool = True
                data4 = {'status': 'false', 'message_4': 'Enter the dob pls'}

            data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4':data4}

            if bool == True:
                print('error check')

                return render(request, 'index.html', {'data': data})

            else:
                print('check else')
                sdetails = StudentDetails(first_name=first_name, last_name=last_name,email_id=email_id, dob=dob)
                sdetails.save()
                print(sdetails.id, 'check sdetails')
            return redirect('/home',{'id':id})


    return render(request, 'index.html', {'sdetails': sdetails})


def home(request):
    sdetails = StudentDetails.objects.all()
    print(sdetails, 'check first name')
    return render(request, 'register_redirect.html', {'sdetails':sdetails})











