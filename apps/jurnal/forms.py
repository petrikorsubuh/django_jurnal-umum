from django import forms
from apps.jurnal import models


class JurnalForm(forms.Form):
    id = forms.CharField(widget= forms.HiddenInput(),required=False)
    nama = forms.CharField(max_length=25,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    keterangan = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control'
    }))

    class Meta:
        model =models.Jurnal