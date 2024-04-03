from django.urls import path
from app1.views import *
app_name='abc'

urlpatterns=[
    path('comment1/',comment1,name='comment1'),
]