from django.shortcuts import render
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


class SongCreateView(CreateView):
    model = models.Song
    form_class = forms.SongForm
    template_name = "music_sc/create_song.html"
    success_url = reverse_lazy("music_sc")


class SongListView(ListView):
    model = models.Song
    template_name = "music_sc/list_songs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Soulcalibur Songs"
        context["now"] = timezone.now()
        context['songs'] = context['object_list']
        return context
