from django.urls import path
from .views import *

urlpatterns = [
    path('',post_list,name='home'),
    path('manage',post_manage,name='post_manage'),
    path('detail/<int:id>',post_detail,name='post_detail'),
    path('delete/<int:id>',post_delete,name='post_delete'),
    path('edit/<int:id>',post_edit,name='post_edit'),
    path('add',post_new,name='post_new'),
    path('category',category_list,name='category_list'),
    #comments
    path('comments/<int:id>',comments,name='comments'),
]
