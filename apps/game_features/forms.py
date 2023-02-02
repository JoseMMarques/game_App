from django import forms

from .models import Complaint


# create a ModelForm
class ComplaintAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplaintAddForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = Complaint
        fields = "__all__"