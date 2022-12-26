import datetime
import os
import pathlib
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


with open(os.path.join(BASE_DIR, "dear_j/secrets.json"), "rb") as secret_file:
    secrets = json.load(secret_file)

# auth setting - user setting
SITE_ID = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"

AUTH_USER_MODEL = "user.User"

# jwt environment setting
REST_USE_JWT = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"
ACCESS_TOKEN_LIFETIME = datetime.timedelta(hours=2)
REFRESH_TOKEN_LIFETIME = datetime.timedelta(days=7)

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATED_LOGOUT_REDIRECTS = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# email verification
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  # 메일 호스트 서버
EMAIL_PORT = "587"  # gmail과 통신하는 포트
EMAIL_HOST_USER = secrets["HOST_MAIL"]["ID"]  # 발신할 이메일
EMAIL_HOST_PASSWORD = secrets["HOST_MAIL"]["PW"]  # 발신할 메일의 비밀번호
EMAIL_USE_TLS = True  # TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # 유저가 받은 링크를 클릭하면 회원가입 완료되게끔
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# 이메일에 자동으로 표시되는 사이트 정보
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Dear J"
