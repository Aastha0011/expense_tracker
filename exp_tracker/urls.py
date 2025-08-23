
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', name='expense', view=views.ExpenseListView.as_view()),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('expenses/add/', views.add_expense, name='add_expense'),
]
