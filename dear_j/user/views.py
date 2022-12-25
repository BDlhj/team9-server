from django import shortcuts
import urllib
import os
import json
from rest_framework import views
from django import http

import jwt

from allauth.socialaccount.providers.kakao import views
from allauth.socialaccount.providers.oauth2 import client
import request
from . import models


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'dear_j/secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)


class KakaoView(views.APIView):
    def get(self, request):
        app_rest_api_key = secrets["KAKAO"]["REST_API_KEY"]
        redirect_uri = secrets["KAKAO"]["MAIN_DOMAIN"] + \
            "login/kakao/callback/"
        return shortcuts.redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
        )


class KakaoCallBackView(views.APIView):
    def get(self, request):
        try:
            data = {
                "grant_type": "authorization_code",
                "client_id": secrets["KAKAO"]["REST_API_KEY"],
                "redirection_uri": secrets["KAKAO"]["MAIN_DOMAIN"] +
                "login/kakao/callback/",
                "code": request.GET["code"]
            }
            kakao_token_api = "https://kauth.kakao.com/oauth/token"
            token_json = request.post(kakao_token_api, data=data).json()

            error = token_json.get("error", None)
            if error is not None:
                return http.JsonResponse({"message": "INVALID_CODE"}, status=400)

            access_token = token_json.get("access_token")

            # get kakaotalk profile information

            profile_request = request.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={
                    "Authorization": f"Bearer {access_token}"
                },
            )
            profile_json = profile_request.json()

            kakao_account = profile_json.get("kakao_account")
            email = kakao_account.get("email", None)
            kakao_id = profile_json.get("id")
        except KeyError:
            return http.JsonResponse(
                {
                    "message": "INVALID_TOKEN"
                },
                status=400)
        except access_token.DoesNotExist:
            return http.JsonResponse({"message": "INVALID_TOKEN"}, status=400)

        kakao_fake_email = kakao_id + "@kakaofake.com"
        if models.User.objects.filter(email=kakao_fake_email).exists():
            user = models.User.objects.get(email=kakao_fake_email)
            token = jwt.encode({"email": kakao_fake_email},
                               secrets["SECRET_KEY"], algorithm="HS256")
            token = token.decode("utf-8")
            return http.JsonResponse({"token": token}, status=200)
        else:
            models.User(
                email=kakao_fake_email
            ).save()
            token = jwt.encode({"email": kakao_fake_email},
                               secrets["SECRET_KEY"], algorithm="HS256")
            token = token.decode("utf-8")
            return http.JsonResponse({"token": token}, status=200)


def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return shortcuts.redirect(f'http://127.0.0.1:8000/account/login/kakao/callback?{params}')
