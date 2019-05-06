from django.shortcuts import render,redirect
from .helpers import *
from django.views import View
from apps.detail import forms
from apps.jurnal.models import Jurnal
from apps.jurnal.forms import JurnalForm
from apps.detail.models import JurnalDetail
from braces.views import LoginRequiredMixin
from  django.http import HttpResponse



class DetailView(View,LoginRequiredMixin):
    login_url = '/login'
    template_name='jurnal_detail.html'

    def get(self, request, jurnal_id):
        detail = JurnalDetail.objects.filter(jurnal_id=jurnal_id)
        total_debt,total_kredit=count_detail(jurnal_id)
        return render(request, self.template_name,{
            'detail':detail,
            'jurnal_id':jurnal_id,
            'total_debt': total_debt,
            'total_kredit': total_kredit
            })

class SaveDetailView(View,LoginRequiredMixin):
    login_url = '/login'

    def post(self, request):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            detail = JurnalDetail()
            detail.tanggal = form.cleaned_data['tanggal']
            detail.deskripsi = form.cleaned_data['deskripsi']
            detail.kredit = form.cleaned_data['kredit']
            detail.debt = form.cleaned_data['debt']
            detail.save()
            return redirect('/detail')


class EditDetailView(View,LoginRequiredMixin):
    login_url = '/login'

    template_name= 'edit_detail.html'

    def get(self, request, jurnal_id, id):
        obj = JurnalDetail.objects.get(id=id)
        form_data = {
            'jurnal_id': jurnal_id,
            'id': obj.id,
            'tanggal': obj.tanggal,
            'deskripsi': obj.deskripsi,
            'kredit': obj.kredit,
            'debt': obj.debt,
        }

        form = forms.DetailForm(initial=form_data)
        data = {
            'form': form,
            'obj':obj,
            'jurnal_id': jurnal_id,
            'a':id,
        }
        return render(request, self.template_name, data)



class UpdateDetailView(View,LoginRequiredMixin):
    login_url = '/login'

    def post(self, request, jurnal_id):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            detail = JurnalDetail.objects.get(id=id)
            detail.tanggal = form.cleaned_data['tanggal']
            detail.deskripsi = form.cleaned_data['deskripsi']
            detail.kredit = form.cleaned_data['kredit']
            detail.debt = form.cleaned_data['debt']
            detail.save()

            url_redirect = f'/detail/{jurnal_id}'
            return redirect(url_redirect)
        return HttpResponse(form.errors)



class DeleteDetailView(View,LoginRequiredMixin):
    login_url = '/login'
    def get(self, request, id,jurnal_id):
        obj = JurnalDetail.objects.get(id=id)
        obj.delete()
        url_redirect = f"/detail/{jurnal_id}"
        return redirect(url_redirect)

class TambahDetailView(View,LoginRequiredMixin):
    login_url = '/login'
    template_name = 'tambah_detail.html'

    def get(self, request, jurnal_id):
        form = forms.DetailForm(request.POST)

        return render(request, self.template_name, {
            'form': form,
            'jurnal_id': jurnal_id
        })

    def post(self, request,jurnal_id):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            jurnal = Jurnal.objects.get(pk=jurnal_id)
            detail = JurnalDetail()
            detail.jurnal= jurnal
            detail.tanggal = form.cleaned_data['tanggal']
            detail.deskripsi = form.cleaned_data['deskripsi']
            detail.kredit = form.cleaned_data['kredit']
            detail.debt = form.cleaned_data['debt']
            detail.save()
            url_redirec = f'/detail/{jurnal_id}'
            return redirect(url_redirec)


        return render(request, self.template_name, {
            'form': form,
            'jurnal_id': jurnal_id
        })