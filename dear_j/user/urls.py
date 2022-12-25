from django import urls


urlpatterns = [
    urls.path("", urls.include("dj_rest_auth.urls")),
    urls.path("", urls.include("allauth.urls")),
    urls.path("", urls.include("django.contrib.auth.urls")),
    urls.path("registration/",
              urls.include("dj_rest_auth.registration.urls"),
              name='registration')
]
