from django.contrib import admin

from .models import (
    Audio, Image, Story, Video
)


def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = "Approve memories"

class MemoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "uploaded_by", "uploaded_at", "approved")
    actions = [approve]    

@admin.register(Story)
class StoryAdmin(MemoryAdmin):
    pass

@admin.register(Image)
class ImageAdmin(MemoryAdmin):
    pass

@admin.register(Video)
class VideoAdmin(MemoryAdmin):
    pass

@admin.register(Audio)
class AudioAdmin(MemoryAdmin):
    pass