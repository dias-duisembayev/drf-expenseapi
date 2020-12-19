from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for a Category model"""

    class Meta:
        model = Category
        fields = ('id', 'name', 'definition')


class ExpenseSerializer(serializers.ModelSerializer):
    """A serializer for a Category model"""

    class Meta:
        model = Expense
        fields = ('id', 'name', 'definition', 'amount', 'created_at')
