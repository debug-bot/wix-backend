
import environ
from .base import *
import os

DEBUG = True

env = environ.Env()
# reading env file
environ.Env.read_env()

SECRET_KEY= env("SECRET_KEY")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "http://127.0.0.1:3000"
]

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': env('CLOUD_NAME'),
#     'API_KEY': env('CLOUD_API_KEY'),
#     'API_SECRET': env('CLOUD_API_SECRET'),
# }
#
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES = {
    'default1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    },
    "default":{
        "ENGINE": "django.db.backends.sqlite3", 
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
}
}

# STRIPE_PUBLISHABLE_KEY=env("STRIPE_PUBLISHABLE_KEY")
# STRIPE_SECRET_KEY=env("STRIPE_SECRET_KEY")

# CURRENT_ADMIN_DOMAIN = env("CURRENT_ADMIN_DOMAIN")
#
# EMAIL_ADMIN = env("EMAIL_ADMIN")

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

STRIPE_PUBLIC_KEY=env("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY=env("STRIPE_SECRET_KEY")
