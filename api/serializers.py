from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    ReadOnlyField,
    CurrentUserDefault,
)
from rest_framework.validators import ValidationError, UniqueTogetherValidator

from .models import (
    Comment,
    Post,
    Follow,
    Group,
    User,
)


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    group = ReadOnlyField(source='group.title')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username',
                            read_only=True,
                            default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    def validate(self, data):
        user = self.context['request'].user
        following = data.get('following')

        if user == following:
            raise ValidationError('You cannot follow to yourself')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='you already followed to the user'
            )
        ]
