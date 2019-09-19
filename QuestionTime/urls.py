from django.contrib import admin
from django.urls import path, include, re_path  # re_path important for single-page app
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView
from user.forms import CustomUserForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", RegistrationView.as_view(form_class=CustomUserForm, success_url="/"),
         name="django_registration_register"),  # custom registration view provided by django via browser
    path("accounts/", include("django_registration.backends.one_step.urls")),  # other django urls package
    path("accounts/", include("django.contrib.auth.urls")),  # login urls provided by django for browser
    path("api/", include("user.api.urls")),
    path("api/", include("questions.api.urls")),
    path("api-auth/", include("rest_framework.urls")),  # login url for browser api
    path("api/rest-auth", include("rest_auth.urls")),   # login endpoint via rest
    path("api/rest-auth/registration", include("rest_auth.registration.urls")),  # registration via rest
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
