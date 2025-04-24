from django.shortcuts import render
from django.utils import timezone
from django.views import View

# Create your views here.


class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        # Add logic
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Seyfer Studios Official Website",
            "now": timezone.now(),
        }
        return render(request, "main/index.html", context)
