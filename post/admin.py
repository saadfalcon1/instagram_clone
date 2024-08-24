from django.contrib import admin
from .models import Post, PostLike, PostComment, CommentLike
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'caption', 'created_time')
    search_fields = ('id', 'username')


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_time')
    search_fields = ('id', 'author__username', 'comment')


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'created_time')
    search_fields = ('id', 'author__username')


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_time')
    search_fields = ('id', 'author__username')


admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
