from django import forms
from . import models


class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = ["order", "name", "type", "game"]


class AlbumSongForm(forms.ModelForm):
    class Meta:
        model = models.AlbumSong
        fields = ["song_number", "album", "song"]


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = [
            'name', 'other_name', 'duration', 'variation_type', 'original_song', "description"
        ]
