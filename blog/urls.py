from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000 --> local
    path('', views.post_list, name='post_list'),

    # http://127.0.0.1:8000/post/2--> local
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # http://127.0.0.1:8000/post/2/new --> local
    path('post/new/', views.post_new, name='post_new'),

    # http://127.0.0.1:8000/post/2/edit --> local
    path('post/<int:pk>/', views.post_edit, name='post_edit'),

    # http://127.0.0.1:8000/post/2/edit --> local
    path('drafts/', views.post_draft_list, name='post_draft'),

    # http://127.0.0.1:8000/post/2/edit --> local
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
]
