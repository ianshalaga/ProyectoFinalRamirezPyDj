from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Game)  # admin.site.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["order", "name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["order"]


@admin.register(models.Album)  # admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["game", "order", "name", "type"]
    search_fields = ["game", "name"]
    list_filter = ["game"]
    ordering = ["order"]


@admin.register(models.Song)  # admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["name", "other_name",
                    "duration", "variation_type", "original_song"]
    search_fields = ["name", "other_name"]
    list_filter = ["variation_type"]
    ordering = ["name"]


@admin.register(models.AlbumSong)  # admin.site.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ["album", "song_number", "song"]
    search_fields = ["song", "album"]
    list_filter = ["album"]
    ordering = ["song_number"]


@admin.register(models.GameMode)  # admin.site.register(GameMode)
class GameModeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(models.Stage)  # admin.site.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["name", "other_name"]
    search_fields = ["name", "other_name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(models.Character)  # admin.site.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(models.Situation)  # admin.site.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]
    list_filter = ["description"]
    ordering = ["description"]
