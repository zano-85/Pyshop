from django.urls import path
from . import views
urlpatterns =[
   path('', views.index1),
   path('new_post', views.new_post)
]