from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.tada_form),
    path('tada/', views.tada_list)
]