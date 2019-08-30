from django import forms

from quizapp.models import StudentDetails


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentDetails
        fields = ['first_name', 'last_name', 'email_id', 'dob']