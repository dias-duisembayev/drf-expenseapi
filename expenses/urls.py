from django.urls import path, re_path

from .views import CategoryList, CategoryDetail, ExpenseList, ExpenseDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/(?P<expense_id>.+)/$', ExpenseDetail.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/$', ExpenseList.as_view()),
    re_path('^categories/(?P<category_id>.+)/$', CategoryDetail.as_view()),
]
