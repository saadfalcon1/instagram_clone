from rest_framework import serializers
from post.models import Post, User, PostLike, PostComment, CommentLike


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = User
        fields = ('photo', 'username', 'id')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    post_likes_count = serializers.SerializerMethodField('get_post_likes_count')
    post_comments_count = serializers.SerializerMethodField('get_post_comments_count')
    me_likes_count = serializers.SerializerMethodField('get_me_likes_count')

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_post_likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def get_post_comments_count(obj):
        return obj.comments.count()

    def get_me_likes_count(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            try:
                PostLike.objects.get(post=obj, author=request.user)
                return True
            except PostLike.DoesNotExist:
                return False
        return False


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField('get_replies')
    me_likes_count = serializers.SerializerMethodField('get_me_likes_count')
    likes_count = serializers.SerializerMethodField('get_likes_count')
    class Meta:
        model = PostComment
        fields = '__all__'
    def get_replies(self, obj):
        if obj.children.exists():
            serializer = self.__class__(obj.children.all(), many=True, context=self.context)
            return serializer.data
        else:
            return None

    def get_me_likes_count(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        else:
            return False

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()


class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = PostLike
        fields = '__all__'


