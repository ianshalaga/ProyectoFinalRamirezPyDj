from django import forms
from . import models


class AlbumSongForm(forms.ModelForm):
    class Meta:
        model = models.AlbumSong
        fields = ["album", "song_number"]


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = [
            'name', 'other_name', 'duration', 'variation_type', 'original_song', "description"
        ]
