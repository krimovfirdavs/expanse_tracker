from config.settings.base import *

import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOCAL_APPS = ["src.core"]
GLOBAL_APPS = [
    "drf_yasg",
    "bootstrap5",
    "rest_framework",
    "django.contrib.humanize",
]
INSTALLED_APPS += LOCAL_APPS + GLOBAL_APPS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ]
}

TIME_ZONE = "Asia/Tashkent"

LOGIN_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/home"
