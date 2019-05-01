from django.contrib import admin
from django.urls import path

from apps.jurnal import views

urlpatterns = [
    path('',views.JurnalView.as_view()),
    path('save',views.SaveJurnalView.as_view(),name='simpan') ,
    path('edit/<int:id>',views.EditJurnalView.as_view(),name='edit') ,
    path('ubah',views.UpdateJurnalView.as_view(),name='ubah') ,
    path('hapus/<int:id>',views.DeleteJurnalView.as_view(),name='hapus') ,
    path('tambah',views.TambahJurnalView.as_view(),name='tambah') ,

]
