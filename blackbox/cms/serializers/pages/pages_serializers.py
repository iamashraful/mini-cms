from rest_framework import serializers

from blackbox.cms.models import Page, Content

__author__ = 'Ashraful'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('identifier', 'status', 'order', 'title', 'body')


class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ('name', 'path', 'contents')
        lookup_field = 'path'
