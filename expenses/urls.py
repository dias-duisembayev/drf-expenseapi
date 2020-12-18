from django.urls import path, re_path

from .views import CategoryCreation, CategoryList, CategoryDetail, ExpenseCreation, ExpenseList, ExpenseDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/create/', CategoryCreation.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/create/$', ExpenseCreation.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/(?P<expense_id>.+)/$', ExpenseDetail.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/$', ExpenseList.as_view()),
    re_path('^categories/(?P<category_id>.+)/$', CategoryDetail.as_view()),
]
