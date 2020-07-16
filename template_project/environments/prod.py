from .components.common import DEBUG,INSTALLED_APPS,DATABASES

DEBUG = False

# set this to your site's hostname/domain names
ALLOWED_HOSTS = ['*',]


## whitenoise production settings

# let whitenoise take over static file serving in production
INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS

## django-compressor
COMPRESS_OFFLINE = True 

## django-storages
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = os.environ.get("DROPBOX_OAUTH2_TOKEN")


## configure database via dj_database_url in prod
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

