from django.shortcuts import render
from expenses.serializers import ExpenseSerializer 
from rest_framework import viewsets      
from expenses.models import Expense
# Create your views here

class ExpenseView(viewsets.ModelViewSet):  
    serializer_class = ExpenseSerializer   
    queryset = Expense.objects.all()    
