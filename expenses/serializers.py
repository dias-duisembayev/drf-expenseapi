from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'definition')


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('id', 'name', 'definition', 'amount', 'created_at')
