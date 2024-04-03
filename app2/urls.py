from django.urls import path
from app2.views import *
app_name='def'

urlpatterns=[
    path('comment2/',comment2,name='comment2'),
]