from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .api import RegisterApi
from . import views
  
urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('login/', views.LoginView.as_view(), name ='login'),
    path('dashboard/', views.DashboardView.as_view(), name ='dashboard'),
    # path('dashboard/', views.dashboardView, name ='dashboard'),
    path('stocks_data/', views.stocksData, name ='stocks_data')
]