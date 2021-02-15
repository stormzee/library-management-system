from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(view_name='BookUpdateDelete', read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author','shelf_number','row_number','date_of_entry','category']

