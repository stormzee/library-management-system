
from django.urls import path
from books.views import add_book,book_category, search_book, update_book, BookAPI, BookUpdate_delete
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
   path('', add_book, name='add_book'),
   path('categories/',book_category, name='categories'),
   path('search/', search_book, name='search'),
   path('update/<int:book_id>/', update_book, name='Update'),
   path('api/', BookAPI.as_view(), name='BookAPI' ),
   path('edit-api/<int:pk>/', BookUpdate_delete.as_view(), name='BookUpdateDelete')
])