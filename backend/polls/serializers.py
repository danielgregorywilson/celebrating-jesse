import datetime

from django.contrib.auth.models import Group, User

from rest_framework import serializers

from polls.models import Audio, Image, Story, Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='get_full_name', required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'password', 'first_name', 'last_name', 'name', 'groups', 'is_staff']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['pk', 'url']


class MemorySerializer(serializers.HyperlinkedModelSerializer):
    uploaded_by_name = serializers.SerializerMethodField()

    @staticmethod
    def get_uploaded_by_name(memory):
        return memory.uploaded_by.get_full_name()

class StorySerializer(MemorySerializer):
    
    class Meta:
        model = Story
        fields = ['pk', 'story', 'title', 'description', 'date', 'age', 'uploaded_by_name']

    def create(self, validated_data):
        story = Story.objects.create(
            story=validated_data['story'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
            age=validated_data.get('age', None)
        )
        if 'date' in validated_data:
            story.date = validated_data['date']
            story.save()
        if Story.objects.filter(uploaded_by__pk=self.context['request'].user.pk, approved=True).count():
            story.approved = True
            story.save()
        return story


class ImageSerializer(MemorySerializer):
    date = serializers.DateField(required=False)

    class Meta:
        model = Image
        fields = ['pk', 'image', 'title', 'description', 'date', 'age', 'uploaded_by_name']
    
    def create(self, validated_data):
        image = Image.objects.create(
            image=validated_data['image'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
            age=validated_data.get('age', None)
        )
        if 'date' in validated_data:
            image.date = validated_data['date']
            image.save()
        if Image.objects.filter(uploaded_by__pk=self.context['request'].user.pk, approved=True).count():
            image.approved = True
            image.save()
        return image


class VideoSerializer(MemorySerializer):

    class Meta:
        model = Video
        fields = ['pk', 'video', 'title', 'description', 'date', 'age', 'uploaded_by_name']
    
    def create(self, validated_data):
        video = Video.objects.create(
            video=validated_data['video'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
            age=validated_data.get('age', None)
        )
        if 'date' in validated_data:
            video.date = validated_data['date']
            video.save()
        if Video.objects.filter(uploaded_by__pk=self.context['request'].user.pk, approved=True).count():
            video.approved = True
            video.save()
        return video


class AudioSerializer(MemorySerializer):

    class Meta:
        model = Audio
        fields = ['pk', 'audio', 'title', 'description', 'date', 'age', 'uploaded_by_name']

    def create(self, validated_data):
        audio = Audio.objects.create(
            audio=validated_data['audio'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
            age=validated_data.get('age', None)
        )
        if 'date' in validated_data:
            audio.date = validated_data['date']
            audio.save()
        if Audio.objects.filter(uploaded_by__pk=self.context['request'].user.pk, approved=True).count():
            audio.approved = True
            audio.save()
        return audio
