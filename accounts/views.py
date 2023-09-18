# from django.conf import settings
from django.contrib.auth import authenticate, login

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return response


# class UserProfileView(LoginRequiredMixin, TemplateView):
#   template_name = "profile.html"


# class LoginView(CreateView):
#    form_class = UserCreationForm
#   template_name = "registration/signup.html"
#    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)  # ここでログイン後のリダイレクトURLを設定

#   def form_valid(self, form):
#        response = super().form_valid(form)
#       login(self.request, self.object)
#       return response
