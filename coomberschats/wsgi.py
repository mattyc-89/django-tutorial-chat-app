"""
WSGI config for coomberschats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import logging
import os

from django.core.wsgi import get_wsgi_application

logger = logging.getLogger(__name__)   # module/class-scoped logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coomberschats.settings')

try:
    application = get_wsgi_application()
except Exception as exc:
    logger.exception(exc)