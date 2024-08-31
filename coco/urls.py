from django.urls import path
from coco import views

urlpatterns=[
    path('info/<int:no>/<int:cost>',views.fun,name='chocalate'),
    path('user',views.userViews,name='userPage'),
    path('check',views.callviews,name='checkPage'),
]