from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_students(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('students:index'))


# def add(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             new_student_number = form.cleaned_data['student_number']
#             new_first_name = form.cleaned_data['student_name']
#             new_last_name = form.cleaned_data['student_last_name']
#             new_email = form.cleaned_data['student_email']
#             new_field_of_study = form.cleaned_data['field_of_study']
#             new_gpa = form.cleaned_data['gpa']
#
#             new_student = Student(
#                 student_number=new_student_number,
#                 first_name=new_first_name,
#                 last_name=new_last_name,
#                 email=new_email,
#                 field_of_study=new_field_of_study,
#                 gpa=new_gpa
#             )
#             new_student.save()
#             return render(request, 'student/add.html',{
#                 'form':StudentForm(),
#                 'success':True,
#             })
#         else:
#             form = StudentForm()
#             return render(request, 'students/add.html', {
#                 'form':StudentForm(),
#             })

def add(request):
    if request.method == 'POST':
        # Initialize form with POST data
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or display a success message
            return render(request, 'students/add.html', {
                'form': StudentForm(),  # Render an empty form
                'success': True,  # Show a success message
            })
    else:
        # Initialize an empty form for GET request
        form = StudentForm()

    # Render the template for GET or invalid POST requests
    return render(request, 'students/add.html', {
        'form': form,
    })
# def edit(request, id):
#     if request.method == 'POST':
#         student = Student.objects.get(pk=id)
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return render(request, 'students/edit.html', {
#                 'form':form,
#                 'success':True,
#             })
#         else:
#             student = Student.objects.get(pk=id)
#             form = StudentForm(instance=student)
#             return render(request, 'students/edit.html', {
#                 'form':form,
#             })

def edit(request, id):
    # Fetch the student object or return a 404 if not found
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        # Bind the form to the POST data and the existing student instance
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Render the form with a success message
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        # Initialize the form for a GET request
        form = StudentForm(instance=student)

    # Render the form for both GET and invalid POST
    return render(request, 'students/edit.html', {
        'form': form,
    })


# def delete(request, id):
#     if request.method == 'POST':
#         student = Student.objects.get(pk=id)
#         student.delete()
#     return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    # Fetch the student object or return a 404 if not found
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        # Redirect to the index page after successful deletion
        return HttpResponseRedirect(reverse('index'))
    # Optionally, handle non-POST requests (e.g., GET requests)
    return HttpResponseRedirect(reverse('index'))
