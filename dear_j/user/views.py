from django import shortcuts
import urllib
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'dear_j/secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)


def kakao_login(request):
    app_rest_api_key = secrets["KAKAO"]["REST_API_KEY"]
    redirect_uri = secrets["KAKAO"]["MAIN_DOMAIN"] + "login/kakao/callback/"
    return shortcuts.redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return shortcuts.redirect(f'http://127.0.0.1:8000/account/login/kakao/callback?{params}')
