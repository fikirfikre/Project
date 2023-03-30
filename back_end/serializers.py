from rest_framework import serializers
from .models import News, Achievements, Officials, ContactUs, Service, Institution, Resource, Article


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image', 'date']


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = ['id', 'title', 'description']


class OfficialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Officials
        fields = ['id', 'name', 'title', 'description',
                  'twitter_links', 'linked_links', 'social_links', 'image']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'suggestion']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image']


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ["id", "title", 'description', 'image']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ["id", "title", "image"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "resource"]
