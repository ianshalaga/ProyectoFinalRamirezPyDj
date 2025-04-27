from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from . import models
from . import forms

# Create your views here.


class MusicScView(View):
    def dispatch(self, request, *args, **kwargs):
        # Add logic
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Soulcalibur Music",
            "now": timezone.now(),
        }
        return render(request, "music_sc/base.html", context)


# @@@@ SONG


class SongListView(ListView):
    model = models.Song
    template_name = "music_sc/song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Soulcalibur Songs"
        context["now"] = timezone.now()
        context['songs'] = context['object_list']
        return context


class SongCreateView(View):
    def dispatch(self, request, *args, **kwargs):
        # Add logic
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        song_form = forms.SongForm()
        albumsong_form = forms.AlbumSongForm()
        context = {
            "title": "Soulcalibur Add Song",
            "now": timezone.now(),
            "song_form": song_form,
            "albumsong_form": albumsong_form
        }
        return render(request, "music_sc/song_create.html", context)

    def post(self, request, *args, **kwargs):
        song_form = forms.SongForm(request.POST)
        albumsong_form = forms.AlbumSongForm(request.POST)
        if song_form.is_valid() and albumsong_form.is_valid():
            song = song_form.save()
            # Asignar la canción recién creada al AlbumSong
            albumsong = albumsong_form.save(commit=False)
            albumsong.song = song
            albumsong.save()
            return redirect("music_sc:music_sc_song_list")
        context = {
            "song_form": song_form,
            "albumsong_form": albumsong_form
        }
        return render(request, "music_sc/song_create.html", context)

    # def put(self, request, *args, **kwargs):
    #     ...

    # def delete(self, request, *args, **kwargs):
    #     ...

    # def patch(self, request, *args, **kwargs):
    #     ...

    # def head(self, request, *args, **kwargs):
    #     ...

    # def options(self, request, *args, **kwargs):
    #     ...


class SongDetailView(DetailView):
    model = models.Song
    template_name = "music_sc/song_detail.html"
    context_object_name = "song"
    slug_field = "code"
    slug_url_kwarg = "code"


# @@@@ ALBUM


class AlbumListView(ListView):
    model = models.Album
    template_name = "music_sc/album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Soulcalibur Albums"
        context["now"] = timezone.now()
        context['albums'] = context['object_list']
        return context


class AlbumCreateView(CreateView):
    model = models.Album
    fields = ["game", "type", "name", "order"]
    template_name = "music_sc/album_create.html"
    success_url = reverse_lazy("music_sc:music_sc_album_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Soulcalibur Albums"
        context["now"] = timezone.now()
        return context
