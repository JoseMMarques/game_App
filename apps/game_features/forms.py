from django import forms
from django.forms.models import ModelChoiceField

from .models import Complaint
from apps.school_structure.models import SchoolClass


# create a ModelForm
class ComplaintAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplaintAddForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = Complaint
        fields = "__all__"


class ComplaintAddFormManual(forms.ModelForm):

    turma = ModelChoiceField(
        queryset=SchoolClass.objects.all(),
        required=True,
        help_text="Turma",
        empty_label="turma",
    )

    class_number = forms.CharField()

    class Meta:
        model = Complaint
        fields = "__all__"
