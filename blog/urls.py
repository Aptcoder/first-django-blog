'''include urls for the blog here'''

from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name = 'post_list')
]