from django import urls
from dj_rest_auth.registration import views as dj_reg_views
from dj_rest_auth import views as dj_views
from . import views


urlpatterns = [
    # login
    urls.path("login/",
              dj_views.LoginView.as_view()),
    urls.path("logout/",
              dj_views.LogoutView.as_view()),
    # registration
    urls.path("registration/",
              dj_reg_views.RegisterView.as_view()),
    urls.path("", urls.include("allauth.urls")),
    # email
    urls.re_path(r"^account-confirm-email/$",
                 dj_reg_views.VerifyEmailView.as_view(),
                 name="account_email_verificaiton_sent"),
    urls.re_path(r"^account-confirm-email/(?P<key>[-:\w]+)/$",
                 views.ConfirmEmailView.as_view(),
                 name="account_confirm_email"),
    # kakao login
    urls.path("login/kakao/", views.kakao_login, name="kakao_login"),
    urls.path("login/kakao/callback/",
              views.kakao_callback, name="kakao_callback"),
]
