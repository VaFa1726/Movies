from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form_add/', views.form_add, name='form_add'),
    path('save_form/', views.add_movie, name='add_movie'),  # نام add_movie اضافه شد
]
