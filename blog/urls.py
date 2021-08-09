from django.urls import path
from . import views
urlpatterns=[
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:id>/', views.post, name='post')
]