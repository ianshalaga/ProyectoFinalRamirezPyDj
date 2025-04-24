from django.shortcuts import render
from django.views import View
from django.utils import timezone

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
