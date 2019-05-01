from django.contrib import admin
from django.urls import path

from apps.detail import views

urlpatterns = [
    path('',views.DetailView.as_view()),
    path('save',views.SaveDetailView.as_view()) ,
    path('edit/<int:id>',views.EditDetailView.as_view()) ,
    path('update',views.UpdateDetailView.as_view()) ,
    path('delete/<int:id>',views.DeleteDetailView.as_view()) ,
    path('tambah',views.TambahDetailView.as_view()) ,

]
