import os
import sys

path = '/home/japhy/tinyPipes-django/'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tinyPipes.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()