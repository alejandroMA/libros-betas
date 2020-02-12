"""
WSGI config for demoDjango2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, '.env')

if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)
else:
    print("cp <root>/.exmple.env <root>/.env")
    sys.exit()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoDjango2.settings')

application = get_wsgi_application()
