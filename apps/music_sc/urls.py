from django.urls import path
from . import views

app_name = "music_sc"

urlpatterns = [
    path("soulcalibur", views.MusicScView.as_view(), name="music_sc"),
]
