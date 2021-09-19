from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.tada_form, name ='employee_tada_add'),
    path('<int:id>/', views.tada_form,name='tada_update'),
    path('delete<int:id>/', views.tada_delete,name='tada_delete'),
    path('list/', views.tada_list, name= 'employee_tada_list'),
    path('tada_pdf', views.generate_pdf, name= 'tada_pdf')


]