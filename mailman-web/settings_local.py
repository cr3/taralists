import os

DEBUG = False

LANGUAGE_CODE = 'fr-ca'

MAILMAN_WEB_SOCIAL_AUTH = []

DEFAULT_FROM_EMAIL = 'mailman@' + os.environ.get('SERVE_FROM_DOMAIN', 'localhost')
