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


class AboutView(View):
    def dispatch(self, request, *args, **kwargs):
        # Add logic
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "title": "About Seyfer Studios",
            "now": timezone.now(),
        }
        return render(request, "main/about.html", context)


def custom404(request, exception, template_name="main/404.html"):
    return render(request, template_name, status=404)


def custom500(request, template_name="main/500.html"):
    return render(request, template_name, status=500)


def custom403(request, exception, template_name="main/403.html"):
    return render(request, template_name, status=403)


def custom400(request, exception, template_name="main/400.html"):
    return render(request, template_name, status=400)
