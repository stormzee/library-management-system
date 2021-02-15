from django.shortcuts import render, redirect, Http404
from books.forms import BookForm, SearchForm

from books.models import Book
from rest_framework import status
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import renderers, permissions,request 
# Create your views here.

def add_book(request):
    
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('search_book')
    return render(request, 'add_book.htm', {'form':form})


def search_book(request):
    form = SearchForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            keyword = form.cleaned_data.get('keyword')
        results = Book.objects.filter(title=keyword)
        print(results)
    return render(request, 'search.htm', {'form':form, 'results':results})
           

def update_book(request, book_id):

    book = Book.objects.get(id=book_id)
    form = BookForm(data= request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.htm', {'form':form})

from main.models import Category

def book_category(request):
    categories = category.objects.get()
    context = {
        'categories':categories
    }

    return render(request, 'categories.htm',context=context)


class BookAPI(APIView):

    def get(self, request, format=None):
        book_list = Book.objects.all()
        # serialize the data(book_list)
        serializer = BookSerializer(book_list, many=True, context={'request':request})
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookUpdate_delete(APIView):

    def get_one(self, request, id):
        try:
            obj = Book.objects.get(pk=id)
            return obj
        except obj.DoesNotExist:
            raise Http404('No book oject Found')

    def get(self, request, pk, format=None):
        book_obj = self.get_one(request, pk)
        serializer = BookSerializer(book_obj, context={'request':request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book_obj = self.get_one(request, pk)
        serializer = BookSerializer(book_obj, data = request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)