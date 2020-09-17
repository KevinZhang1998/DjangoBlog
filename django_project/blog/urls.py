from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # PostListView 不能直接使用
    path('', PostListView.as_view(), name='blog-home'),  # views.home 返回HTTP响应的结果
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # views.home 返回HTTP响应的结果
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # views.home 返回HTTP响应的结果
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # views.home 返回HTTP响应的结果
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]
