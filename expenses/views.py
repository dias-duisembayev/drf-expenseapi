from rest_framework import generics, permissions

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from .permissions import IsCategoryOwner


class CategoryList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner=user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner,)
    serializer_class = CategorySerializer

    def get_object(self):
        category_id = self.kwargs['category_id']
        obj = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, obj)
        return obj


class ExpenseList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner)
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user = self.request.user
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, category)
        return Expense.objects.filter(category=category_id, category__owner=user)


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner)
    serializer_class = ExpenseSerializer

    def get_object(self):
        user = self.request.user
        category_id = self.kwargs['category_id']
        expense_id = self.kwargs['expense_id']
        category = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, category)
        obj = Expense.objects.get(id=expense_id, category__owner=user, category__id=category_id)
        return obj
