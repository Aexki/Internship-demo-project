from django.shortcuts import render
from .models import student
# Create your views here.


def student_info(request):
    if request.method == "POST":
        s = student()
        s.name = request.POST['name']
        birthday = request.POST['bday']
        s.gender = request.POST['gender']
        s.email = request.POST['email']
        s.phone = request.POST['phone']
        s.birthday = birthday[-4:]+'-'+birthday[3:5]+'-'+birthday[:2]
        s.save()

    return render(request, 'index.html')
