from django.urls import path

from .views import CategoryList, CategoryDetail, ExpenseList, ExpenseDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('expenses/', ExpenseList.as_view()),
    path('expenses/<int:pk>/', ExpenseDetail.as_view()),
]
