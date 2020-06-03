from django.urls import path
from PaymentsDemo import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generateTrainingModel/', views.generateTrainingModel, name='generateTrainingModel'),
    path('generateTrainingModel/<str:custId>/', views.trainData, name='generateTrainingModelFor'),
    path('test/', views.testPaymentTransaction, name='testPaymentTransaction'),
  
]
