from django.urls import path,include
from main.views import *

urlpatterns = [
    path('news/',NewsAPIList.as_view()),
    path('news/<int:pk>/', NewsAPIUpdate.as_view()),
    path('newsdelete/<int:pk>/', NewsAPIDestroy.as_view()),
    path('register/', RegisterAPIList.as_view()),
    path('registerdelete/<int:pk>/', RegisterAPIDestroy.as_view()),
]
