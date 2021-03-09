from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    group = serializers.ReadOnlyField(source='group.title')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate(self, data):
        user = self.context['request'].user
        following = data.get('following')

        if user == following:
            raise ValidationError('You cannot follow to yourself')

        if Follow.objects.filter(user__username=user,
                                 following__username=following).exists():
            raise ValidationError(
                f'You already followed to {data.get("following")}')

        return data

    class Meta:
        fields = '__all__'
        model = Follow
