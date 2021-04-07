from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import (
    BasePermission, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated,
    IsAuthenticatedOrReadOnly, SAFE_METHODS
)
from rest_framework.response import Response

from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404

from polls.models import Audio, Image, Story, Video


from polls.serializers import (
    AudioSerializer, GroupSerializer, ImageSerializer, StorySerializer,
    UserSerializer, VideoSerializer
)

class CurrentUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [IsAdminOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsAdminOrReadOnly]


class MemoryPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # Override to include the number of pages
        response = super(MemoryPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class StoryPagination(MemoryPagination):
    page_size = 4


class ImagePagination(MemoryPagination):
    page_size = 20


class VideoPagination(MemoryPagination):
    page_size = 2


class AudioPagination(MemoryPagination):
    page_size = 2


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.filter(approved=True)
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StoryPagination


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.filter(approved=True)
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ImagePagination


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.filter(approved=True)
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = VideoPagination


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.filter(approved=True)
    serializer_class = AudioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = AudioPagination
