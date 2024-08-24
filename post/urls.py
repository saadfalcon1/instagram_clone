from django.urls import path
from .views import (PostListAPIView, PostCreateAPIView, PostCommentCreateAPIView, PostLikeListAPIView,
                    PostRetrieveUpdateDestroyAPIView, CommentListCreateAPIView,
                    PostCommentListAPIView, CommentRetrieveAPIView, CommentLikeListAPIView)

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
    path('posts/<uuid:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<uuid:pk>/comments/', PostCommentListAPIView.as_view()),
    path('posts/<uuid:pk>/comments/create/', PostCommentCreateAPIView.as_view()),
    path('posts/comments/', CommentListCreateAPIView.as_view()),
    path('posts/<uuid:pk>/likes/', PostLikeListAPIView.as_view()),
    path('posts/comments/<uuid:pk>/', CommentRetrieveAPIView.as_view()),
    path('posts/comments/<uuid:pk>/likes/', CommentLikeListAPIView.as_view())

]