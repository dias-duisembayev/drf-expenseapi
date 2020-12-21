from django.urls import path, re_path

from .views import CategoryCreation, CategoryList, CategoryDetail, \
    ExpenseCreation, ExpenseListAll, ExpenseListByCategory, ExpenseDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/create/', CategoryCreation.as_view()),
    path('categories/expenses/all/', ExpenseListAll.as_view()),
    re_path('^categories/expenses/all/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})/$', ExpenseListAll.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/create/$', ExpenseCreation.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/(?P<expense_id>.+)/$', ExpenseDetail.as_view()),
    re_path('^categories/(?P<category_id>.+)/expenses/$', ExpenseListByCategory.as_view()),
    re_path('^categories/(?P<category_id>.+)/$', CategoryDetail.as_view()),
]
