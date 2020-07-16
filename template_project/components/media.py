## media files - user uploaded files while the website is running
import os
from template_project.components.common import BASE_DIR

MEDIA_URL = "/media/"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

