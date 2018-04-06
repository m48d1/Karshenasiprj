"""
WSGI config for Karshenasi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

path='/var/wwww/html/Karshenasi'

if path not in sys.path:
  sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Karshenasi.settings")

application = get_wsgi_application()
