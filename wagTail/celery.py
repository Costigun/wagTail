from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wagTail.settings')

celery_app = Celery('wagTail')
celery_app.config_from_object('django.conf:settings',namespace='CELERY')
celery_app.autodiscover_tasks()