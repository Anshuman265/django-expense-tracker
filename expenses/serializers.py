from rest_framework import serializers
from expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id' ,'title', 'amount', 'date')