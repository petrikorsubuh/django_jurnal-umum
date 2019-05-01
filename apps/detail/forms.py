from django import forms
from apps.detail import models
import datetime

class DateInput(forms.Form):
    input_type = 'date'


class DetailForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput(),required=False)
    tanggal = forms.DateField(
        initial =datetime.date.today,widget= DateInput
    )
    deskripsi = forms.CharField(required = True,widget=forms.Textarea)
    kredit = forms.FloatField(required=False,initial=0)
    debt = forms.FloatField(required=False,initial=0)
