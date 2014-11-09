
import sae
from langcolor import wsgi
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'langcolor.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'langcolor'))


application = sae.create_wsgi_app(wsgi.application)
