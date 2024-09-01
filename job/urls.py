from django.urls import path
from . import views
from . import api

app_name='job'
urlpatterns=[
    path('',views.job_list,name='job_list'),
    path('add_job',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_details'), 
    path('<str:slug>/like_unlike',views.like_unlike,name='like_unlike'), 
    
    #rest_framework
    path('api/fbv/',api.fbv_list,name='fbv_list'),
    path('api/fbv/<int:pk>',api.fbv_pk,name='fbv_pk'),
    
    path('api/generic/',api.generic_list.as_view(),name='generic_list'),
    path('api/generic/<int:pk>',api.generic_pk.as_view(),name='generic_pk')
]