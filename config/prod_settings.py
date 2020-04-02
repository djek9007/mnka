import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x-n#*(4klrjw34*OOHN7678^%$#$%^&*(m@h86&^i8v6qwyljsa*w#!m(2)b1x5**elwm*i)'

DEBUG = False

ALLOWED_HOSTS = ["mnka.kz", "http:mnka.kz"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'course',
        'USER': 'john',
        'PASSWORD': 'Q12klk()d75&8*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'zakaz@mnka.kz'
EMAIL_HOST_PASSWORD = 'r2KC8UDZavfa'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True