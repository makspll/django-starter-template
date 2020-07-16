import os
from template_project.components.common import BASE_DIR

## Static files base settings (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# source files at top level are included
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static_src") # original files
]


# destination for all static files in their final compressed/cached/preprocessed form
STATIC_ROOT = os.path.join(BASE_DIR,'static_root')

## Whitenoise base settings

# enables compression and caching support and CDN ready static serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# remove unnecessary file copies
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

## django-compressor

# pre-process scss and sass files
COMPRESS_PRECOMPILERS = [
    ("text/x-scss", "django_libsass.SassCompiler"),
    ('text/x-sass',"django_libsass.SassCompiler")]

COMPRESS_CACHEABLE_PRECOMPILERS = (
    ("text/x-scss", "django_libsass.SassCompiler"),
    ('text/x-sass',"django_libsass.SassCompiler"))


# filters to apply to js and css files
JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter', # minify js
]
CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter', # make url() absolutes
    'compressor.filters.cssmin.CSSMinFilter', # minify css
    ]

COMPRESS_FILTERS={
    'css':CSS_FILTERS,
    'js':JS_FILTERS,
}

# use brotli compression
COMPRESS_STORAGE = 'compressor.storage.BrotliCompressorFileStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # others 

    # /
    'compressor.finders.CompressorFinder',
)
