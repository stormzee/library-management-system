from django.shortcuts import render, redirect

# Create your views here.
from .forms import StudentForm


def create_student(request):

    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'create_student.htm', {'form':form})

def borrow(request):

    pass


