from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_students(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('students:index'))
