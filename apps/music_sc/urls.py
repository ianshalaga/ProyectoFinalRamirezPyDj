from django.urls import path
from . import views

app_name = "music_sc"

urlpatterns = [
    # Base
    path("soulcalibur/", views.MusicScView.as_view(), name="music_sc"),
    # Song
    path("soulcalibur/song/list/",
         views.SongListView.as_view(), name="music_sc_song_list"),
    path("soulcalibur/song/create/",
         views.SongCreateView.as_view(), name="music_sc_song_create"),
    path("soulcalibur/song/detail/<uuid:code>",
         views.SongDetailView.as_view(), name="music_sc_song_detail"),
    path("soulcalibur/song/update/<uuid:code>",
         views.SongUpdateView.as_view(), name="music_sc_song_update"),
    path("soulcalibur/song/delete/<uuid:code>",
         views.SongDeleteView.as_view(), name="music_sc_song_delete"),
    # Album
    path("soulcalibur/album/list/",
         views.AlbumListView.as_view(), name="music_sc_album_list"),
    path("soulcalibur/album/create/",
         views.AlbumCreateView.as_view(), name="music_sc_album_create"),
]
