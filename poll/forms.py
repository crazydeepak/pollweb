from django import forms

from .models import Monitor


class MonitorForm(forms.Form):

    class Meta:
        model = Monitor
        fields = '__all__'
