from django.db import models

# Create your models here.
from main.models import User
from books.models import Book
from users.models import Student

class Borrow(models.Model):

    librarian = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s'%(self.librarian.username, self.student.name)