from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime

from .models import Category, Expense


class CategoryTest(TestCase):
    """A Test class for testing a Category model"""

    @classmethod
    def setUpTestData(cls):
        """Setting up a test user and a Category owned by that user"""
        test_user = User.objects.create_user(username='test_user', password='123123')
        test_user.save()

        test_category = Category.objects.create(
            name='category_test_name', definition='category_test_definition', owner=test_user)
        test_category.save()

    def test_category_content(self):
        """Asserting contents of the Category"""
        category = Category.objects.get(id=1)
        name = f'{category.name}'
        definition = f'{category.definition}'
        owner = f'{category.owner}'
        self.assertEqual(name, 'category_test_name')
        self.assertEqual(definition, 'category_test_definition')
        self.assertEqual(owner, 'test_user')


class ExpenseTest(TestCase):
    """A Test class for testing an Expense model"""

    @classmethod
    def setUpTestData(cls):
        """Setting up multiple users, Categories and an Expense"""
        test_user = User.objects.create_user(username='test_user', password='123123')
        test_user.save()
        test_unused_user = User.objects.create_user(username='test_unused_user', password='123123')
        test_unused_user.save()

        test_category = Category.objects.create(
            name='category_test_name', definition='category_test_definition', owner=test_user)
        test_category.save()
        test_unused_category = Category.objects.create(
            name='unused', definition='unused', owner=test_unused_user)
        test_unused_category.save()

        test_expense = Expense.objects.create(
            name='expense_test_name', definition='expense_test_definition', category=test_category,
            amount=999.999, created_at=datetime(2020, 1, 1))
        test_expense.save()

    def test_expense_owner(self):
        """Testing Expense owner trough FK relation of Expense's Category"""
        expense = Expense.objects.get(id=1)
        category = expense.category
        self.assertEqual(f'{category.owner}', 'test_user')

    def test_expense_content(self):
        """Asserting contents of the Expense"""
        expense = Expense.objects.get(id=1)
        name = f'{expense.name}'
        definition = f'{expense.definition}'
        category_name = f'{expense.category.name}'
        amount = expense.amount
        created_at = expense.created_at
        self.assertEqual(name, 'expense_test_name')
        self.assertEqual(definition, 'expense_test_definition')
        self.assertEqual(category_name, 'category_test_name')
        self.assertEqual(amount, 999.999)
        self.assertEqual(created_at, datetime(2020, 1, 1).date())
