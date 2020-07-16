from template_project.components.common import INSTALLED_APPS,MIDDLEWARE,BASE_DIR
import debug_toolbar
from django.urls import path,include
import os 

INSTALLED_APPS =  INSTALLED_APPS + [
    'debug_toolbar',]


MEDIA_ROOT = os.path.join(BASE_DIR,"media_root")

## django-debug-toolbar
# for evaluating query performance 

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

DEFAULT_URL_PATTERNS = [ 
    path('__debug__/',include(debug_toolbar.urls))
]

INTERNAL_IPS = [
    '127.0.0.1',
]

## email setup
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
