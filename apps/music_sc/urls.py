from django.urls import path
from . import views

app_name = "music_sc"

urlpatterns = [
    path("soulcalibur/", views.MusicScView.as_view(), name="music_sc"),
    path("soulcalibur/songs/list/",
         views.SongListView.as_view(), name="music_sc_list"),
    path("soulcalibur/song/create/",
         views.SongCreateView.as_view(), name="music_sc_create")
]
