from django import forms

from .models import Complaint


# create a ModelForm
class ComplaintAddForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = "__all__"