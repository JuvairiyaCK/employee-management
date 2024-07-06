from .models import EmpData
from django import forms


class EmpForm(forms.ModelForm):
    class Meta:
        model=EmpData
        fields="__all__"
        widget={
            "ename":forms.TextInput(attrs={"class":"form-control","placeholder":"enter employee name"}),
             "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter age"}),
             "salary":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter salary"}),
             "designation":forms.TextInput(attrs={"class":"form-control","placeholder":"enter designation"})
        }