from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """A Category model"""
    name = models.CharField(max_length=50)
    definition = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'owner',)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """An Expense model"""
    name = models.CharField(max_length=50)
    definition = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateField()

    class Meta:
        unique_together = ('name', 'category',)

    def __str__(self):
        return self.name
