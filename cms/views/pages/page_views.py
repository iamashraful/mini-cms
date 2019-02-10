import uuid

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import AllowAny

from cms.models import Page
from cms.serializers.pages.pages_serializers import PageListSerializer, PageDetailsSerializer

__author__ = 'Ashraful'


class PageListView(generics.ListCreateAPIView):
    serializer_class = PageListSerializer
    permission_classes = (AllowAny,)
    queryset = Page.objects.order_by('order')


class PageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageDetailsSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            uuid.UUID(slug)
            _obj = Page.objects.get(path=slug)
            return _obj
        except (ValueError, ObjectDoesNotExist):
            return None
