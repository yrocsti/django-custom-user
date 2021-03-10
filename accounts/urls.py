from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
]
