from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:projectid>/', views.detail, name='detail'),
    path('<int:projectid>/upvote1/', views.upvote1, name='upvote1'),
    path('<int:projectid>/downvote1/', views.downvote1, name='downvote1'),
    path('<int:projectid>/upvote2/', views.upvote2, name='upvote2'),
    path('<int:projectid>/downvote2/', views.downvote2, name='downvote2'),
]
