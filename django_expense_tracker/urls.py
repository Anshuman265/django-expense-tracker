
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers                 
from expenses import views

router = routers.DefaultRouter()                   
router.register(r'expenses', views.ExpenseView, 'Expense') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), #http://localhost:8000/api/expenses/ all expenses here  
]
