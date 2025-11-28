"""
WSGI config for recipe_sharing_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Ensure media directories exist
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / 'media'
RECIPES_DIR = MEDIA_ROOT / 'recipes'
PROFILES_DIR = MEDIA_ROOT / 'profiles'

# Create directories if they don't exist
MEDIA_ROOT.mkdir(exist_ok=True)
RECIPES_DIR.mkdir(exist_ok=True)
PROFILES_DIR.mkdir(exist_ok=True)

application = get_wsgi_application()





