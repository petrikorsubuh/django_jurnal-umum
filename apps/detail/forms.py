from django import forms
from apps.detail import models
from  apps.jurnal.models import  Jurnal
import datetime


class DetailForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput(),required=False)
    tanggal = forms.DateField(label='Tanggal',
        initial =datetime.date.today,widget= forms.DateInput()
    )
    deskripsi = forms.CharField(label='Deskripsi',required = True,widget=forms.TextInput)
    kredit = forms.FloatField(label='Kredit',required=False,initial=0)
    debt = forms.FloatField(label='Debt',required=False,initial=0)
