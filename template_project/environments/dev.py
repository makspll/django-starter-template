from .components.common import INSTALLED_APPS,MIDDLEWARE
import debug_toolbar
from django.urls import path,include

INSTALLED_APPS = ['livesync',] + INSTALLED_APPS + [
    'debug_toolbar',]


# MIDDLEWARE_CLASSES = (
#     'livesync.core.middleware.DjangoLiveSyncMiddleware',
# )
## django-debug-toolbar
# for evaluating query performance 

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware','livesync.core.middleware.DjangoLiveSyncMiddleware']

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