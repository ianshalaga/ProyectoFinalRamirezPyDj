from django.utils import timezone
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    next_page = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Seyfer Studios Login"
        context["now"] = timezone.now()
        return context


class CustomLogoutView(View):
    template_name = 'user/logout.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        # Add logic
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Seyfer Studios Logout",
            "now": timezone.now(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.success_url)


class CustomSignupView(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        avatar_image = self.request.FILES.get('avatar')
        if avatar_image:
            models.Avatar.objects.create(user=self.object, image=avatar_image)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Seyfer Studios Register"
        context["now"] = timezone.now()
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['avatar'] = self.request.user.avatar.image.url
        except:
            context['avatar'] = None
        context['title'] = "User Profile"
        context['now'] = timezone.now()
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('user:user_detail')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user_before = self.request.user
        response = super().form_valid(form)

        avatar_image = self.request.FILES.get('avatar')
        if avatar_image:
            avatar, created = models.Avatar.objects.get_or_create(
                user=self.request.user)
            avatar.image = avatar_image
            avatar.save()

        # new_password = form.cleaned_data.get('password')
        # if new_password:
        #     login(self.request, self.object)

        return response


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'user/password_change.html'
    success_url = reverse_lazy('user:password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cambiar Contraseña - Seyfer Studios"
        context["now"] = timezone.now()
        return context
