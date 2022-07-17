from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
