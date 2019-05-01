from django.shortcuts import render,redirect

from django.views import View

from apps.detail import models
from apps.detail import forms
from braces.views import LoginRequiredMixin

class LoginDulu(LoginRequiredMixin):
    login_url='/login' 


class DetailView(View,LoginDulu):
    template_name='jurnal_detail.html'

    def get(self, request, id):
        obj=models.JurnalDetail.get(id=id)
        

class SaveDetailView(View,LoginDulu):

    def post(self, request):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            detail = models.JurnalDetail()
            detail.item = form.cleaned_data['item']
            detail.kredit = form.cleaned_data['kredit']
            detail.save()
            return redirect('/detail')


class EditDetailView(View,LoginDulu):

    template_name= 'Edit_detail.html'

    def get(self, request, id):
        obj = models.JurnalDetail.objects.get(id=id)
        data = {
            'id': obj.id,
            'item': obj.item,
            'kredit': obj.kredit,
        }

        form = forms.DetailForm(initial=data)
        detail = models.JurnalDetail.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'detail': detail
        })



class UpdateDetailView(View,LoginDulu):

    def post(self, request):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            detail = models.Jurnal.objects.get(id=form.cleaned_data['id'])
            detail.item = form.cleaned_data['item']
            detail.kredit = form.cleaned_data['kredit']
            detail.save()
            
            return redirect('/detail')
        return HttpResponse(form.errors)



class DeleteDetailView(View,LoginDulu):
    # login_url = '/login'
    def get(self, request, id):
        obj = models.JurnalDetail.objects.get(id=id)
        obj.delete()

        return redirect('/detail')



class TambahDetailView(View,LoginDulu):
    # login_url = '/login'
    template_name = 'tambah_detail.html'

    def get(self, request):
        form = forms.DetailForm(request.POST)
        detail = models.JurnalDetail.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'detail': detail
        })

    def post(self, request):
        form = forms.JurnalForm(request.POST)
        if form.is_valid():
            jurnal = models.Jurnal()
            jurnal.nama = form.cleaned_data['nama']
            jurnal.save()
            
            return redirect('/jurnal')
        return HttpResponse(form.errors)