from django import forms
from .models import JobCard


class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = [
            'PropertieID',
            'CustomerClickID',
            'CustomerID',
            'StatusID',
            'RoleID',
            'RegionID',
        ]

















