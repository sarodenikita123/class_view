from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "employee_id": forms.NumberInput(),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "branch ": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.RadioSelect(),
            "salary": forms.NumberInput(),
            "join_date": forms.DateInput(),
            "address": forms.TextInput(attrs={"class": "form-control"})
        }