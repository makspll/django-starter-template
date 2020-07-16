from split_settings.tools import optional, include
import os

ENV = os.environ.get("DJANGO_ENV",'dev') 

BASE_SETTINGS = [
    'components/common.py',
    'components/languages.py',
    'components/database.py',
    'components/media.py',
    'components/static.py',
    'environments/{0}.py'.format(ENV),
    optional('environments/local.py'),
]


include(*BASE_SETTINGS)