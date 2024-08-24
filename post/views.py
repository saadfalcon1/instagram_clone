from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .models import Post, PostLike, PostComment, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer
from shared.custom_pagination import CustomPagination
from rest_framework.response import Response


# Create your views here.


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'code': status.HTTP_200_OK,
                'message': 'Post successfully updated',
                'data': serializer.data
            }
        )

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(
            {
                'success': True,
                'code': status.HTTP_200_OK,
                'message': 'Post successfully deleted',
                'data': None
            }
        )


class PostCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = PostComment.objects.filter(post__id=post_id)
        return queryset


class PostCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(author=self.request.user, post_id=post_id)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = PostComment.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [AllowAny, ]
    queryset = PostComment.objects.all()


class PostLikeListAPIView(generics.ListAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [AllowAny, ]
    def get_queryset(self):
        post_id = self.kwargs['pk']
        return PostLike.objects.filter(post_id=post_id)


class CommentLikeListAPIView(generics.ListAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [AllowAny, ]
    def get_queryset(self):
        comment_id = self.kwargs['pk']
        return CommentLike.objects.filter(comment_id=comment_id)



