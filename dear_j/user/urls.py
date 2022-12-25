from django import urls
from . import views


urlpatterns = [
    urls.path("", urls.include("dj_rest_auth.urls")),
    urls.path("", urls.include("allauth.urls")),
    urls.path("", urls.include("django.contrib.auth.urls")),
    urls.path("registration/",
              urls.include("dj_rest_auth.registration.urls"),
              name='registration'),
    urls.path("login/kakao/", views.kakao_login, name="kakao_login"),
    urls.path("login/kakao/callback/",
              views.kakao_callback, name="kakao_callback"),
]
