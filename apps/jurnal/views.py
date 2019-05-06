from django.shortcuts import render,redirect
from django.views import View
from apps.jurnal import models
from apps.jurnal import forms
from braces.views import  StaffuserRequiredMixin,LoginRequiredMixin


class JurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    template_name = 'jurnal.html'
    login_url = '/login'

    def get(self, request):
        form = forms.JurnalForm(request.POST)
        jurnal = models.Jurnal.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'jurnal': jurnal
        })


class SaveJurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    login_url = '/login'

    def post(self, request):
        jur = forms.JurnalForm(request.POST)
        if jur.is_valid():
            jurnal = models.Jurnal()
            jurnal.nama  = jur.cleaned_data['nama']
            jurnal.user  = request.user
            jurnal.keterangan  = jur.cleaned_data['keterangan']
            jurnal.save()
            return redirect('/jurnal')
        


class EditJurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    login_url = '/login'
    template_name = 'edit_jurnal.html'

    def get(self, request, id):
        obj = models.Jurnal.objects.get(id=id)
        data = {
            'id': obj.id,
            'nama': obj.nama,
            'keterangan': obj.keterangan,
        }

        form = forms.JurnalForm(initial=data)
        jurnal = models.Jurnal.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'jurnal': jurnal
        })


class UpdateJurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    login_url = '/login'
    def post(self, request):
        form = forms.JurnalForm(request.POST)
        if form.is_valid():
            jurnal = models.Jurnal.objects.get(id=form.cleaned_data['id'])
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save(force_update=True)
            
            return redirect('/jurnal')
        return HttpResponse(form.errors)


class DeleteJurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    login_url = '/login'
    def get(self, request, id):
        obj = models.Jurnal.objects.get(id=id)
        obj.delete()

        return redirect('/jurnal')

class TambahJurnalView(View,LoginRequiredMixin,StaffuserRequiredMixin):
    login_url = '/login'
    template_name = 'tambah_jurnal.html'

    def get(self, request):
        form = forms.JurnalForm(request.POST)
        jurnal = models.Jurnal.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'jurnal': jurnal
        })

    def post(self, request):
        form = forms.JurnalForm(request.POST)
        if form.is_valid():
            jurnal = models.Jurnal()
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save()
            
            return redirect('/jurnal')
        return HttpResponse(form.errors)
