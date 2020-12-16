from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'definition', 'owner')


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('name', 'definition', 'category', 'amount', 'created_at')
