from django import forms
from .models import Task, Employee


class TaskAdminForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=False,
        label="Assign to Employee"
    )

    class Meta:
        model = Task
        fields = '__all__'
