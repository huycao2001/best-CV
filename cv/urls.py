from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.index, name='home'),
    path('create/<idTemplate>', views.create_cv, name='create-cv'),
    path('templates/', views.choose_template, name='choose-template'),
    path('cv/<id>/', views.cv_detail, name='cv'),
    path('cv-delete/<id>/', views.cv_delete, name='cv-delete'),
    path('edit-cv/<id>/', views.cv_edit, name='cv-edit'),
    path('search-expenses', csrf_exempt(views.search_expenses),
         name="search_expenses")
]
