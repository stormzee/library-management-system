from django.db import models

from main.models import Category
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shelf_number = models.PositiveIntegerField()
    row_number = models.PositiveIntegerField()
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s written by %s'%(self.title, self.author)

    class Meta:
        verbose_name_plural = 'Books'
