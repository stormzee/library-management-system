from django.shortcuts import render, redirect
from .forms import BorrowForm
# Create your views here.
def borrow(request):
    
    form = BorrowForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'Borrow.htm', {'form':form})