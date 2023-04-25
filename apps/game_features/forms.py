from django import forms
from django.forms.models import ModelChoiceField

from .models import Complaint, ParecerDT
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

    class Meta:
        model = Complaint
        exclude = ['user', 'qualidade', 'dt', 'estado', 'slug', 'parecer_dt']
        widgets = {
            'dia': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                },
            ),
            'hora': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                },
            ),
        }


class ParecerAddForm(forms.ModelForm):

    class Meta:
        model = ParecerDT
        exclude = ['dt', 'complaint', 'slug']
