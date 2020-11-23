from django.urls import path
from . import views

urlpatterns = [
    path('', views.EIAhome, name='EIA-home'),
    path('EIAquery.html', views.EIAquery, name='EIA-query'),
]