from rest_framework import generics, permissions

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from .permissions import IsCategoryOwner


class CategoryCreation(generics.CreateAPIView):
    """A view used to create a single instance of a Category"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Performs create for a Category class with predefined owner field as request' user"""
        serializer.save(owner=self.request.user)


class CategoryList(generics.ListAPIView):
    """A view for listing all Categories used by request's user"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Returns a queryset which consists all Categories owned by request's user"""
        user = self.request.user
        return Category.objects.filter(owner=user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """A view for showing a user's single Category"""
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner,)
    serializer_class = CategorySerializer

    def get_object(self):
        """Returns a request's user's Category according to 'id' field """
        category_id = self.kwargs['category_id']
        obj = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, obj)
        return obj


class ExpenseCreation(generics.CreateAPIView):
    """A view used to create a single instance of an Expense"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        """Performs create for a Expense class with predefined category"""
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)


class ExpenseListByCategory(generics.ListAPIView):
    """A view for listing all Expenses of a particular Category"""
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner)
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        """Returns a queryset with all user's Expenses in a particular Category"""
        user = self.request.user
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, category)
        return Expense.objects.filter(category=category_id, category__owner=user)


class ExpenseListAll(generics.ListAPIView):
    """A view for listing a user's all Expenses"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        """Return a query set of a user's all expenses ordered by created_at field (descending)"""
        user = self.request.user
        return Expense.objects.filter(category__owner=user).order_by('-created_at')


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    """A view for showing a user's single Expense"""
    permission_classes = (permissions.IsAuthenticated, IsCategoryOwner)
    serializer_class = ExpenseSerializer

    def get_object(self):
        """Returns a user's single Expense object according to category and id fields"""
        user = self.request.user
        category_id = self.kwargs['category_id']
        expense_id = self.kwargs['expense_id']
        category = Category.objects.get(id=category_id)
        self.check_object_permissions(self.request, category)
        obj = Expense.objects.get(id=expense_id, category__owner=user, category__id=category_id)
        return obj
