from django.contrib import admin
from django.urls import path

from apps.detail import views

urlpatterns = [
    path('<int:jurnal_id>',views.DetailView.as_view()),
    path('<int:jurnal_id>/save',views.SaveDetailView.as_view(),name='save') ,
    path('<int:jurnal_id>/edit/<int:id>',views.EditDetailView.as_view(),name='edit') ,
    path('<int:jurnal_id>/update',views.UpdateDetailView.as_view(),name='update') ,
    path('<int:jurnal_id>/delete/<int:id>',views.DeleteDetailView.as_view(),name='delete') ,
    path('<int:jurnal_id>/tambah',views.TambahDetailView.as_view(),name='tambah') ,

]
