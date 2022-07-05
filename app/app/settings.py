import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
LISTEN_PORT = int(os.environ.get("LISTEN_PORT", 8000))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "info")
