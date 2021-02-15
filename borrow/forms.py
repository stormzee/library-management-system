from django.forms import ModelForm
from .models import Borrow


class BorrowForm(ModelForm):

    class Meta:
        model = Borrow
        fields = "__all__"